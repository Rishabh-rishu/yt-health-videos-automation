#!/usr/bin/env python3
"""
Direct YouTube Upload Utility for Rendered Health Videos
Uploads an existing, QC-passed video to YouTube with private status.
"""

import sys
import os
from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parent.parent
venv_python = ROOT_PATH / "venv" / "bin" / "python3"
if (sys.prefix == sys.base_prefix) and venv_python.exists():
    os.execv(str(venv_python), [str(venv_python)] + sys.argv)

import argparse
import logging
from typing import Optional

# Add project root to sys.path
sys.path.insert(0, str(ROOT_PATH))

from database.db_manager import DatabaseManager
from youtube.publisher import YouTubePublisher
from youtube.metadata_generator import MetadataGenerator

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("health_videos.upload_short")

def upload_rendered_short(topic_id: str, custom_visibility: Optional[str] = None):
    db = DatabaseManager()
    
    # 1. Fetch calendar entry and topic details
    cal_entry = db.get_calendar_entry(topic_id)
    topic_data = db.get_topic(topic_id)
    
    if not cal_entry and not topic_data:
        logger.error(f"Topic ID '{topic_id}' not found in content calendar or topics database.")
        sys.exit(1)
        
    title = (cal_entry or topic_data).get("title")
    category = (cal_entry or topic_data).get("category", "General Health")
    core_science = (cal_entry or topic_data).get("core_concept") or (topic_data or {}).get("research_summary", "")
    sources = (cal_entry or topic_data).get("research_sources", [])
    
    # 2. Check video file
    video_path_str = (cal_entry or topic_data).get("video_path")
    if not video_path_str or not Path(video_path_str).exists():
        # Fallback to standard path
        standard_path = ROOT_PATH / "output" / "videos" / f"{topic_id}_health_short.mp4"
        if standard_path.exists():
            video_path = standard_path
        else:
            logger.error(f"Rendered video file not found for topic '{topic_id}'. Searched: {video_path_str} and {standard_path}")
            sys.exit(1)
    else:
        video_path = Path(video_path_str)
        
    # 3. Check thumbnail file
    thumb_path = ROOT_PATH / "output" / "thumbnails" / f"{topic_id}_thumb.jpg"
    if not thumb_path.exists():
        thumb_path = None
        
    logger.info(f"Target Video: {video_path} ({video_path.stat().st_size} bytes)")
    if thumb_path:
        logger.info(f"Target Thumbnail: {thumb_path}")

    # 4. Generate SEO Metadata
    meta_gen = MetadataGenerator()
    metadata = meta_gen.generate_metadata(
        title=title,
        category=category,
        core_science=core_science,
        sources=sources if isinstance(sources, list) else []
    )
    
    logger.info(f"Upload Title: {metadata['title']}")
    logger.info(f"Category ID: {metadata['categoryId']}")

    # 5. Execute YouTube Upload
    publisher = YouTubePublisher(db=db)
    result = publisher.publish_video(
        topic_id=topic_id,
        video_path=video_path,
        metadata=metadata,
        thumbnail_path=thumb_path,
        force_upload=True
    )
    
    if result.get("status") == "success":
        video_id = result.get("video_id")
        video_url = result.get("url")
        visibility = result.get("visibility")
        
        print("\n" + "=" * 65)
        print("  🎉 YOUTUBE SHORT UPLOADED SUCCESSFULLY!")
        print("=" * 65)
        print(f"  Channel:     Swasth Snap (@swasthsnapyt)")
        print(f"  Topic ID:    {topic_id}")
        print(f"  Title:       {metadata['title']}")
        print(f"  Video ID:    {video_id}")
        print(f"  Visibility:  {visibility} (Safe Staging for User Review)")
        print(f"  Watch URL:   {video_url}")
        print(f"  Studio URL:  https://studio.youtube.com/video/{video_id}/edit")
        print("=" * 65 + "\n")
        return result
    else:
        logger.error(f"Upload failed: {result}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload rendered short to YouTube")
    parser.add_argument("--topic-id", type=str, default="day01_video01", help="Topic ID to upload (default: day01_video01)")
    args = parser.parse_args()
    
    upload_rendered_short(topic_id=args.topic_id)
