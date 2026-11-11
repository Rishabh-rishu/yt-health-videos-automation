#!/usr/bin/env python3
"""
Production & YouTube Upload Cron Job Runner for Health Videos
Executes scheduled 2x daily production (09:30 AM IST and 18:00 PM IST).
Guarantees:
- Strict topic anti-repetition via SQLite calendar & topic deduplication.
- Chronological execution through the 15-day (30-topic) content bank.
- Automatic rendering and YouTube upload with comprehensive logging.
"""

import sys
import os
from pathlib import Path
from datetime import datetime

ROOT_PATH = Path(__file__).resolve().parent.parent
venv_python = ROOT_PATH / "venv" / "bin" / "python3"
if (sys.prefix == sys.base_prefix) and venv_python.exists():
    os.execv(str(venv_python), [str(venv_python)] + sys.argv)

import argparse
import logging
import pytz

# Add project root to sys.path
sys.path.insert(0, str(ROOT_PATH))

from config.settings import TIMEZONE, LOGS_DIR
from database.db_manager import DatabaseManager
from youtube.upload_short import upload_rendered_short
from main import produce_health_short

LOGS_DIR.mkdir(parents=True, exist_ok=True)
cron_log_file = LOGS_DIR / "cron_production.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(cron_log_file, encoding="utf-8")
    ]
)
logger = logging.getLogger("health_videos.cron_runner")

LOCK_FILE = ROOT_PATH / ".cron_job.lock"

def acquire_lock() -> bool:
    if LOCK_FILE.exists():
        # Check if process is still alive or stale lock
        try:
            pid = int(LOCK_FILE.read_text().strip())
            os.kill(pid, 0)
            logger.warning(f"Another production job is already running with PID {pid}. Skipping execution.")
            return False
        except (ValueError, OSError):
            logger.info("Overwriting stale cron lock file.")
    LOCK_FILE.write_text(str(os.getpid()))
    return True

def release_lock():
    if LOCK_FILE.exists():
        try:
            LOCK_FILE.unlink()
        except Exception:
            pass

def run_scheduled_job(dry_run: bool = False, force_topic: str = None):
    tz = pytz.timezone(TIMEZONE)
    now_str = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S %Z")
    
    logger.info("=" * 65)
    logger.info(f"HEALTH VIDEOS CRON EXECUTION STARTED AT: {now_str}")
    logger.info("=" * 65)
    
    if not acquire_lock():
        return False

    try:
        db = DatabaseManager()
        
        # 1. Identify target topic
        if force_topic:
            target_entry = db.get_calendar_entry(force_topic)
            if not target_entry:
                logger.error(f"Specified forced topic '{force_topic}' not found in calendar.")
                return False
        else:
            target_entry = db.get_next_pending_calendar_entry()

        if not target_entry:
            logger.info("All 30 topics in the 15-day content calendar have been published!")
            logger.info("Discovering fresh dynamic topic via TopicDiscoveryEngine with anti-repetition...")
            if dry_run:
                logger.info("[DRY RUN] Would discover new topic via AI and execute.")
                return True
            success, topic_id, video_path = produce_health_short(force_upload=True)
            logger.info(f"Dynamic topic completed: {topic_id} -> {video_path}")
            return success

        topic_id = target_entry["topic_id"]
        title = target_entry["title"]
        day_num = target_entry["day_number"]
        video_num = target_entry["video_number"]
        render_status = target_entry.get("render_status")
        approval_status = target_entry.get("approval_status")
        video_path_str = target_entry.get("video_path")

        logger.info(f"Target Scheduled Topic: Day {day_num} Video #{video_num}")
        logger.info(f"Topic ID: {topic_id} | Title: \"{title}\"")
        logger.info(f"Current State: render_status={render_status}, approval_status={approval_status}")

        # Strict Anti-Repetition Gate
        if approval_status == "UPLOADED":
            logger.warning(f"Topic {topic_id} is already marked as UPLOADED. Skipping to prevent duplicate upload.")
            return True

        if dry_run:
            logger.info(f"[DRY RUN] Target topic confirmed: {topic_id} ('{title}'). Ready for execution.")
            return True

        # Check if already rendered and verified
        video_exists = video_path_str and Path(video_path_str).exists()
        if render_status == "RENDERED" and video_exists:
            logger.info(f"Video is already rendered at {video_path_str}. Proceeding directly to YouTube upload...")
            result = upload_rendered_short(topic_id=topic_id)
            if result.get("status") == "success":
                logger.info(f"Scheduled video published successfully: {result.get('url')}")
                return True
            else:
                logger.error(f"Failed to upload existing video for {topic_id}.")
                return False
        else:
            logger.info(f"Producing, rendering and uploading Short for {topic_id}...")
            success, produced_id, video_path = produce_health_short(
                topic_id=topic_id,
                category=target_entry.get("category", "General Health"),
                force_upload=True
            )
            if success:
                logger.info(f"Successfully produced and published {produced_id} to YouTube!")
                return True
            else:
                logger.error(f"Production pipeline failed for {topic_id}.")
                return False

    except Exception as e:
        logger.exception(f"Unhandled exception in cron job runner: {e}")
        return False
    finally:
        release_lock()
        logger.info(f"Cron execution finished at: {datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S %Z')}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Health Videos Cron Job Runner")
    parser.add_argument("--dry-run", action="store_true", help="Simulate execution without modifying or uploading")
    parser.add_argument("--topic-id", type=str, default=None, help="Force execution of a specific topic ID")
    args = parser.parse_args()

    success = run_scheduled_job(dry_run=args.dry_run, force_topic=args.topic_id)
    sys.exit(0 if success else 1)
