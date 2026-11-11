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
        
        try:
            from database.state_sync import restore_state
            restore_state(self.db_path)
        except Exception as e:
            logger.debug(f"Restore state check: {e}")

    def _sync_state(self):
        try:
            from database.state_sync import export_state
            export_state(self.db_path)
        except Exception as e:
            logger.debug(f"State sync warning: {e}")

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
        self._sync_state()
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
        self._sync_state()

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

    # -------------------------------------------------------------
    # BGM Usage & Anti-Repetition Methods
    # -------------------------------------------------------------
    def record_bgm_usage(self, track_id: str, track_category: str, topic_id: Optional[str] = None, duration_seconds: float = 0.0):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO bgm_history (track_id, track_category, topic_id, duration_seconds)
                VALUES (?, ?, ?, ?)
            """, (track_id, track_category, topic_id, duration_seconds))
            conn.commit()
            logger.info(f"Recorded BGM usage: {track_id} ({track_category}) for topic {topic_id}")

    def get_recent_bgm_tracks(self, limit: int = 5) -> List[str]:
        """Returns the last N track_ids used to prevent repetition."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT track_id FROM bgm_history
                ORDER BY id DESC LIMIT ?
            """, (limit,))
            return [row["track_id"] for row in cursor.fetchall()]

    # -------------------------------------------------------------
    # Video Originality & History Tracking Methods
    # -------------------------------------------------------------
    def record_video_history(self, video_data: Dict[str, Any]) -> str:
        """Stores comprehensive video fingerprint and visual metadata for 100% originality enforcement."""
        video_id = video_data.get("video_id") or f"vid_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO video_history (
                    video_id, topic_id, main_topic, subtopic, core_scientific_concept,
                    script_text, hook_text, title, scene_descriptions, visual_asset_ids,
                    models_animations, camera_angles_movements, lighting_style, subtitle_text,
                    bgm_track_id, rendered_path, clean_shorts_path, video_fingerprint,
                    originality_score, publishing_status
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                video_id,
                video_data.get("topic_id"),
                video_data.get("main_topic") or video_data.get("title", ""),
                video_data.get("subtopic", ""),
                video_data.get("core_scientific_concept") or video_data.get("research_summary", ""),
                video_data.get("script_text", ""),
                video_data.get("hook_text") or video_data.get("hook", ""),
                video_data.get("title", ""),
                json.dumps(video_data.get("scene_descriptions", []), ensure_ascii=False),
                json.dumps(video_data.get("visual_asset_ids", []), ensure_ascii=False),
                json.dumps(video_data.get("models_animations", []), ensure_ascii=False),
                json.dumps(video_data.get("camera_angles_movements", []), ensure_ascii=False),
                video_data.get("lighting_style", "cinematic_dark_glow"),
                video_data.get("subtitle_text", ""),
                video_data.get("bgm_track_id", ""),
                video_data.get("rendered_path", ""),
                video_data.get("clean_shorts_path", ""),
                video_data.get("video_fingerprint", ""),
                video_data.get("originality_score", 1.0),
                video_data.get("publishing_status", "draft")
            ))
            conn.commit()
        self._sync_state()
        logger.info(f"Recorded video history for {video_id} (Fingerprint: {video_data.get('video_fingerprint', '')[:12]}...)")
        return video_id

    def get_all_past_topics(self) -> List[Dict[str, Any]]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT topic_id, title, category, hook, research_summary, script_text FROM topics")
            return [dict(row) for row in cursor.fetchall()]

    def get_all_past_videos(self) -> List[Dict[str, Any]]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM video_history ORDER BY creation_date DESC")
            rows = []
            for r in cursor.fetchall():
                d = dict(r)
                for field in ["scene_descriptions", "visual_asset_ids", "models_animations", "camera_angles_movements"]:
                    if d.get(field):
                        try:
                            d[field] = json.loads(d[field])
                        except Exception:
                            pass
                rows.append(d)
            return rows

    # -------------------------------------------------------------
    # Rejected Generation Attempts Tracking
    # -------------------------------------------------------------
    def record_rejected_attempt(
        self,
        attempt_type: str,
        content_payload: Any,
        rejection_reason: str,
        similarity_score: float = 0.0,
        matched_entity_id: Optional[str] = None
    ) -> int:
        payload_str = json.dumps(content_payload, ensure_ascii=False) if isinstance(content_payload, (dict, list)) else str(content_payload)
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO rejected_attempts (
                    attempt_type, content_payload, rejection_reason,
                    similarity_score, matched_entity_id
                ) VALUES (?, ?, ?, ?, ?)
            """, (attempt_type, payload_str, rejection_reason, similarity_score, matched_entity_id))
            conn.commit()
            return cursor.lastrowid

    def get_recent_rejected_attempts(self, attempt_type: Optional[str] = None, limit: int = 20) -> List[Dict[str, Any]]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            if attempt_type:
                cursor.execute("""
                    SELECT * FROM rejected_attempts WHERE attempt_type = ?
                    ORDER BY attempted_at DESC LIMIT ?
                """, (attempt_type, limit))
            else:
                cursor.execute("""
                    SELECT * FROM rejected_attempts
                    ORDER BY attempted_at DESC LIMIT ?
                """, (limit,))
            return [dict(row) for row in cursor.fetchall()]

    # -------------------------------------------------------------
    # 15-Day Content Calendar Methods (30 Unique Educational Videos)
    # -------------------------------------------------------------
    def upsert_calendar_entry(self, entry: Dict[str, Any]) -> str:
        topic_id = entry["topic_id"]
        sources = entry.get("research_sources", [])
        sources_json = json.dumps(sources, ensure_ascii=False) if isinstance(sources, list) else str(sources)
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO content_calendar (
                    day_number, video_number, topic_id, title, category, core_concept,
                    hook_text, term_key, scientific_term, term_badge_title, term_badge_sub,
                    research_sources, visual_style_prompt, bgm_category, research_status,
                    script_status, voice_status, visual_status, render_status, qc_status,
                    approval_status, video_path, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            """, (
                entry["day_number"],
                entry["video_number"],
                topic_id,
                entry["title"],
                entry["category"],
                entry["core_concept"],
                entry["hook_text"],
                entry.get("term_key", ""),
                entry.get("scientific_term", ""),
                entry.get("term_badge_title", ""),
                entry.get("term_badge_sub", ""),
                sources_json,
                entry.get("visual_style_prompt", ""),
                entry.get("bgm_category", "medical_documentary"),
                entry.get("research_status", "VERIFIED"),
                entry.get("script_status", "PLANNED"),
                entry.get("voice_status", "PLANNED"),
                entry.get("visual_status", "PLANNED"),
                entry.get("render_status", "PLANNED"),
                entry.get("qc_status", "PLANNED"),
                entry.get("approval_status", "STAGED"),
                entry.get("video_path", "")
            ))
            conn.commit()
        self._sync_state()
        return topic_id

    def get_calendar_entry(self, topic_id: str) -> Optional[Dict[str, Any]]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM content_calendar WHERE topic_id = ?", (topic_id,))
            row = cursor.fetchone()
            if row:
                d = dict(row)
                if d.get("research_sources"):
                    try: d["research_sources"] = json.loads(d["research_sources"])
                    except Exception: pass
                return d
            return None

    def update_calendar_stage(self, topic_id: str, **kwargs):
        """Updates specific workflow status fields (e.g. script_status, render_status, video_path)."""
        fields = ["updated_at = CURRENT_TIMESTAMP"]
        values = []
        for key, val in kwargs.items():
            fields.append(f"{key} = ?")
            if isinstance(val, (dict, list)):
                val = json.dumps(val, ensure_ascii=False)
            values.append(val)
        values.append(topic_id)
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"UPDATE content_calendar SET {', '.join(fields)} WHERE topic_id = ?", values)
            conn.commit()
        self._sync_state()

    def get_all_calendar_entries(self) -> List[Dict[str, Any]]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM content_calendar ORDER BY video_number ASC")
            rows = []
            for r in cursor.fetchall():
                d = dict(r)
                if d.get("research_sources"):
                    try: d["research_sources"] = json.loads(d["research_sources"])
                    except Exception: pass
                rows.append(d)
            return rows

    def get_next_pending_calendar_entry(self) -> Optional[Dict[str, Any]]:
        """
        Retrieves the next calendar entry that has not been uploaded yet.
        Enforces strict chronological sequence: Video #1 to #30.
        Prevents repetition by filtering out approval_status = 'UPLOADED'.
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM content_calendar 
                WHERE approval_status != 'UPLOADED' 
                ORDER BY video_number ASC 
                LIMIT 1
            """)
            row = cursor.fetchone()
            if row:
                d = dict(row)
                if d.get("research_sources"):
                    try: d["research_sources"] = json.loads(d["research_sources"])
                    except Exception: pass
                return d
            return None



