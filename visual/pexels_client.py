"""
Pexels Stock Video Client for Medical & Relatable B-Roll
Fetches 1080x1920 or 1920x1080 licensed scientific & human footage.
"""

import os
import json
import logging
import requests
from pathlib import Path
from typing import Optional, Dict, Any, List

from config.settings import PEXELS_API_KEY, ASSETS_DIR

logger = logging.getLogger("health_videos.pexels")

NEGATIVE_KEYWORDS = [
    "hospital", "patient", "clinic", "mask", "surgery",
    "bedridden", "doctor mask", "chemotherapy", "beaker",
    "doctor", "nurse", "syringe", "needle", "ward",
    "stretcher", "operating room", "wheelchair"
]

class PexelsClient:
    def __init__(self, api_key: str = PEXELS_API_KEY):
        self.api_key = api_key
        self.cache_dir = ASSETS_DIR / "visual_cache"
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _is_safe_video(self, video: Dict[str, Any]) -> bool:
        """Checks if a video contains any negative/irrelevant keywords."""
        url_text = video.get("url", "").lower().replace("-", " ")
        tags = [t.lower() for t in video.get("tags", []) if isinstance(t, str)]
        combined_text = f"{url_text} {' '.join(tags)}"

        for neg in NEGATIVE_KEYWORDS:
            if neg in combined_text:
                logger.debug(f"Rejecting Pexels video {video.get('id')} due to negative keyword: '{neg}'")
                return False
        return True

    def search_video(self, query: str, orientation: str = "portrait") -> Optional[str]:
        """
        Searches Pexels for a video matching the query.
        Filters out clinical/hospital imagery with negative keywords.
        Downloads and caches the video file.
        Returns path to local MP4 or None.
        """
        safe_query = query.replace(" ", "_").lower()
        cached_file = self.cache_dir / f"{safe_query}.mp4"
        if cached_file.exists() and cached_file.stat().st_size > 100000:
            return str(cached_file)

        headers = {"Authorization": self.api_key}
        url = f"https://api.pexels.com/videos/search?query={query}&per_page=8&orientation={orientation}"
        
        try:
            resp = requests.get(url, headers=headers, timeout=12)
            videos = []
            if resp.status_code == 200:
                videos = resp.json().get("videos", [])

            if not videos:
                # Try landscape orientation if portrait query was empty
                url_land = f"https://api.pexels.com/videos/search?query={query}&per_page=8"
                resp = requests.get(url_land, headers=headers, timeout=12)
                if resp.status_code == 200:
                    videos = resp.json().get("videos", [])

            if not videos:
                logger.warning(f"No Pexels video found for query: '{query}'")
                return None

            # Filter out hospital / clinic / patient imagery
            safe_videos = [v for v in videos if self._is_safe_video(v)]
            if not safe_videos:
                logger.warning(f"All Pexels videos for '{query}' contained negative keywords. Falling back.")
                return None

            selected_video = safe_videos[0]

            # Choose best quality HD/FHD file
            best_link = None
            for f in selected_video.get("video_files", []):
                if f.get("width", 0) >= 1080 or f.get("height", 0) >= 1080:
                    best_link = f["link"]
                    break
            if not best_link and selected_video.get("video_files"):
                best_link = selected_video["video_files"][0]["link"]

            if best_link:
                logger.info(f"Downloading verified Pexels clip for '{query}' -> {cached_file.name}")
                v_resp = requests.get(best_link, stream=True, timeout=20)
                with open(cached_file, "wb") as f:
                    for chunk in v_resp.iter_content(chunk_size=65536):
                        f.write(chunk)
                return str(cached_file)
        except Exception as e:
            logger.error(f"Error fetching Pexels video for '{query}': {e}")
            return None

