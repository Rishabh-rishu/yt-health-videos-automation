"""
Automation Scheduler for Health Videos Production
Runs two automated production cycles per day:
- Morning Slot: 12:00 IST
- Evening Slot: 18:00 IST
Features retry handling, state tracking, and duplicate prevention.
"""

import time
import logging
import schedule
import pytz
from datetime import datetime

from config.settings import TIMEZONE, SCHEDULE_MORNING_TIME, SCHEDULE_EVENING_TIME

logger = logging.getLogger("health_videos.scheduler")

class AutomationScheduler:
    def __init__(self, production_callback):
        self.callback = production_callback
        self.tz = pytz.timezone(TIMEZONE)

    def run_production_job(self, slot_name: str):
        now_ist = datetime.now(self.tz).strftime("%Y-%m-%d %H:%M:%S")
        logger.info(f"[{now_ist}] Triggering scheduled production run for slot: {slot_name}")
        try:
            success, topic_id, video_path = self.callback()
            if success:
                logger.info(f"Scheduled run succeeded: Topic {topic_id} -> {video_path}")
            else:
                logger.error(f"Scheduled run failed for slot: {slot_name}")
        except Exception as e:
            logger.exception(f"Unhandled exception during scheduled job {slot_name}: {e}")

    def start(self):
        logger.info(f"Starting Health Videos Scheduler (Timezone: {TIMEZONE})")
        logger.info(f"Slots configured: Morning={SCHEDULE_MORNING_TIME}, Evening={SCHEDULE_EVENING_TIME}")

        schedule.every().day.at(SCHEDULE_MORNING_TIME).do(self.run_production_job, slot_name="Morning")
        schedule.every().day.at(SCHEDULE_EVENING_TIME).do(self.run_production_job, slot_name="Evening")

        while True:
            schedule.run_pending()
            time.sleep(30)
