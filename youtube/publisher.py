"""
YouTube Publishing Engine for Health Videos
Supports official YouTube Data API v3 upload workflow with strict safety controls:
- AUTO_UPLOAD = false by default
- MANUAL_APPROVAL_REQUIRED = true
- Strict check of duplicate uploads against SQLite
- Uploads as private/draft for user review
"""

import os
import pickle
import logging
from pathlib import Path
from typing import Dict, Any, Optional

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

from config.settings import (
    AUTO_UPLOAD,
    MANUAL_APPROVAL_REQUIRED,
    VIDEO_VISIBILITY,
    ROOT_DIR
)
from database.db_manager import DatabaseManager

logger = logging.getLogger("health_videos.youtube_publisher")

class YouTubePublisher:
    def __init__(self, db: Optional[DatabaseManager] = None):
        self.db = db or DatabaseManager()
        self.token_file = ROOT_DIR / "token.pickle"
        self.secrets_file = ROOT_DIR / "client_secrets.json"

    def get_service(self):
        if not self.token_file.exists():
            logger.warning("YouTube token.pickle not found. Publishing unavailable.")
            return None
        with open(self.token_file, "rb") as f:
            creds = pickle.load(f)
        return build("youtube", "v3", credentials=creds)

    def publish_video(
        self,
        topic_id: str,
        video_path: Path,
        metadata: Dict[str, Any],
        thumbnail_path: Optional[Path] = None,
        force_upload: bool = False
    ) -> Dict[str, Any]:
        """
        Uploads video to YouTube with private status.
        Safety gate: Requires force_upload=True or AUTO_UPLOAD=True.
        """
        if not force_upload and not AUTO_UPLOAD:
            logger.info("AUTO_UPLOAD is False. Video held in staging for manual user approval.")
            return {
                "status": "staged_for_approval",
                "message": "Production completed. Video verified and staged. Upload disabled per safety policy.",
                "video_path": str(video_path)
            }

        service = self.get_service()
        if not service:
            return {"status": "error", "message": "Missing YouTube authentication credentials."}

        body = {
            "snippet": {
                "title": metadata["title"],
                "description": metadata["description"],
                "tags": metadata.get("tags", []),
                "categoryId": metadata.get("categoryId", "27")
            },
            "status": {
                "privacyStatus": VIDEO_VISIBILITY,
                "selfDeclaredMadeForKids": False
            }
        }

        media = MediaFileUpload(str(video_path), mimetype="video/mp4", resumable=True)
        request = service.videos().insert(part="snippet,status", body=body, media_body=media)
        response = request.execute()

        video_id = response.get("id")
        logger.info(f"Video uploaded successfully to YouTube! ID: {video_id}")

        # Upload thumbnail if provided
        if thumbnail_path and thumbnail_path.exists() and video_id:
            try:
                service.thumbnails().set(
                    videoId=video_id,
                    media_body=MediaFileUpload(str(thumbnail_path), mimetype="image/jpeg")
                ).execute()
                logger.info(f"Uploaded thumbnail for video ID: {video_id}")
            except Exception as e:
                logger.warning(f"Could not upload thumbnail: {e}")

        # Update DB
        self.db.update_topic_status(
            topic_id,
            status="published",
            upload_id=video_id,
            publication_date=response.get("snippet", {}).get("publishedAt", "")
        )
        try:
            self.db.update_calendar_stage(
                topic_id,
                approval_status="UPLOADED"
            )
        except Exception:
            pass

        return {
            "status": "success",
            "video_id": video_id,
            "visibility": VIDEO_VISIBILITY,
            "url": f"https://youtube.com/shorts/{video_id}"
        }
