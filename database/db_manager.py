"""
SQLite Database Manager for Health Videos
Handles topic tracking, deduplication, sentence scene mapping, and audit logging.
"""

import sqlite3
import json
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime

from config.settings import DB_PATH, DATABASE_DIR

logger = logging.getLogger("health_videos.db")

class DatabaseManager:
    def __init__(self, db_path: Path = DB_PATH):
        self.db_path = db_path
        DATABASE_DIR.mkdir(parents=True, exist_ok=True)
        self.init_db()

    def get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(str(self.db_path))
        conn.row_factory = sqlite3.Row
        return conn

    def init_db(self):
        schema_file = DATABASE_DIR / "schema.sql"
        if schema_file.exists():
            with open(schema_file, "r", encoding="utf-8") as f:
                schema_sql = f.read()
            with self.get_connection() as conn:
                conn.executescript(schema_sql)
                conn.commit()
            logger.info("Database initialized successfully.")

    def is_topic_duplicate(self, title: str) -> bool:
        """Checks if a topic title or close variant already exists in DB."""
        clean_title = title.lower().strip()
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM topics WHERE LOWER(title) = ? OR LOWER(title) LIKE ?", 
                           (clean_title, f"%{clean_title}%"))
            return cursor.fetchone() is not None

    def save_topic(self, topic_data: Dict[str, Any]) -> str:
        """Saves a newly researched topic."""
        topic_id = topic_data.get("topic_id")
        sources = topic_data.get("research_sources") or topic_data.get("sources") or []
        sources_json = json.dumps(sources, ensure_ascii=False)
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO topics (
                    topic_id, title, category, hook, hook_style, research_summary,
                    research_sources, evidence_status, script_text, status, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            """, (
                topic_id,
                topic_data.get("title"),
                topic_data.get("category"),
                topic_data.get("hook"),
                topic_data.get("hook_style"),
                topic_data.get("core_science") or topic_data.get("research_summary"),
                sources_json,
                topic_data.get("evidence_status", "verified"),
                topic_data.get("script_text"),
                topic_data.get("status", "discovered")
            ))
            conn.commit()
        return topic_id

    def update_topic_status(self, topic_id: str, status: Optional[str] = None, **kwargs):
        """Updates status and additional fields of a topic."""
        fields = ["updated_at = CURRENT_TIMESTAMP"]
        values = []
        if status:
            fields.append("status = ?")
            values.append(status)
        for key, val in kwargs.items():
            fields.append(f"{key} = ?")
            if isinstance(val, (dict, list)):
                val = json.dumps(val, ensure_ascii=False)
            values.append(val)
        values.append(topic_id)
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"UPDATE topics SET {', '.join(fields)} WHERE topic_id = ?", values)
            conn.commit()

    def save_sentence_scenes(self, topic_id: str, scenes: List[Dict[str, Any]]):
        """Saves visual specification for each sentence in the timeline."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM sentence_scenes WHERE topic_id = ?", (topic_id,))
            for idx, scene in enumerate(scenes):
                text = scene.get("sentence") or scene.get("sentence_text") or ""
                cursor.execute("""
                    INSERT INTO sentence_scenes (
                        topic_id, sentence_idx, sentence_text, start_sec, end_sec,
                        visual_description, visual_type, camera_movement, animation_notes,
                        overlay_text, asset_path
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    topic_id,
                    idx,
                    text,
                    scene.get("start_sec", 0.0),
                    scene.get("end_sec", 0.0),
                    scene.get("visual_description", ""),
                    scene.get("visual_type", "3d_anatomy"),
                    scene.get("camera_movement", "slow_push"),
                    scene.get("animation_notes", ""),
                    scene.get("text_overlay", ""),
                    scene.get("asset_path", "")
                ))
            conn.commit()

    def get_topic(self, topic_id: str) -> Optional[Dict[str, Any]]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM topics WHERE topic_id = ?", (topic_id,))
            row = cursor.fetchone()
            if row:
                d = dict(row)
                if d.get("research_sources"):
                    try:
                        d["research_sources"] = json.loads(d["research_sources"])
                    except Exception:
                        pass
                return d
            return None

    def get_sentence_scenes(self, topic_id: str) -> List[Dict[str, Any]]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM sentence_scenes WHERE topic_id = ? ORDER BY sentence_idx ASC", (topic_id,))
            return [dict(row) for row in cursor.fetchall()]
