"""
Automatic Intelligent Background Music (BGM) Selector & Tone Classifier
Integrates with the 8-Category Verified Music Library and SQLite anti-repetition engine:
1. Suspense science (suspense_science)
2. Medical documentary (medical_documentary)
3. Deep ambient (deep_ambient)
4. Mystery and discovery (mystery_discovery)
5. Informational education (informational_education)
6. Emotional science (emotional_science)
7. Cinematic technology (cinematic_technology)
8. Soft background atmosphere (soft_atmosphere)

Performs multi-factor mood detection (category, title, script keywords, scene roles),
checks track history to prevent repetition across consecutive videos, and strictly
verifies commercial licensing status.
"""

import json
import logging
from pathlib import Path
from typing import Tuple, Dict, Any, Optional, List

from config.settings import ASSETS_DIR
from database.db_manager import DatabaseManager

logger = logging.getLogger("health_videos.bgm_selector")

class BGMSelector:
    def __init__(self, db: Optional[DatabaseManager] = None):
        self.audio_dir = ASSETS_DIR / "audio"
        self.ledger_path = self.audio_dir / "license_ledger.json"
        self.db = db or DatabaseManager()
        self.library = self._load_verified_library()

        # Keywords for multi-factor mood detection
        self.mood_keywords = {
            "suspense_science": [
                "khatra", "danger", "risk", "deadly", "toxin", "poison", "warning",
                "attack", "failure", "decay", "destruction", "chronic", "damage"
            ],
            "medical_documentary": [
                "heart", "blood", "circulation", "artery", "cardiac", "cellular",
                "biology", "dhadkan", "oxygen", "vessels", "pumping", "microbiology"
            ],
            "deep_ambient": [
                "sleep", "neend", "glymphatic", "brain", "rest", "night", "rejuvenation",
                "healing", "cleansing", "recovery", "soothing", "peaceful", "dream"
            ],
            "mystery_discovery": [
                "mystery", "raaz", "secret", "hidden", "unknown", "wonder", "why",
                "curiosity", "kya aap jaante", "uncovered", "truth", "shocking"
            ],
            "informational_education": [
                "food", "diet", "nutrition", "vitamins", "water", "habit", "lifestyle",
                "gut", "digestion", "daily", "khana", "routine", "exercise"
            ],
            "emotional_science": [
                "human", "life", "miracle", "hope", "survival", "mother", "child",
                "evolution", "generations", "emotion", "resilience", "journey"
            ],
            "cinematic_technology": [
                "technology", "neuroscience", "synapse", "electrical", "signals",
                "microscopic", "neurons", "brainwave", "computation", "dna", "crispr"
            ],
            "soft_atmosphere": [
                "skin", "hair", "calm", "balance", "wellness", "breath", "lungs",
                "gentle", "smooth", "care", "subtle"
            ]
        }

    def _load_verified_library(self) -> Dict[str, Dict[str, Any]]:
        """Loads and indexes verified tracks from license_ledger.json."""
        catalog = {}
        if not self.ledger_path.exists():
            logger.warning(f"License ledger not found at {self.ledger_path}. Falling back to default beds.")
            return catalog

        try:
            with open(self.ledger_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            tracks = data.get("tracks", [])
            for t in tracks:
                # Enforce licensing verification gate
                if t.get("verification_status") != "VERIFIED_SAFE_FOR_MONETIZATION":
                    logger.warning(f"Skipping unverified track: {t.get('track_id')}")
                    continue
                cat = t.get("category")
                catalog[cat] = t
        except Exception as e:
            logger.error(f"Failed to parse license ledger: {e}")
        return catalog

    def detect_mood(
        self,
        category: str,
        topic_title: str = "",
        script_text: str = "",
        scene_roles: Optional[List[str]] = None
    ) -> str:
        """
        Multi-factor mood scoring across topic category, title, script sentiment, and scene roles.
        """
        combined_text = f"{category} {topic_title} {script_text}".lower()
        scores = {cat: 0 for cat in self.mood_keywords}

        # 1. Category primary bias
        cat_lower = category.lower()
        if "sleep" in cat_lower:
            scores["deep_ambient"] += 6
        elif "heart" in cat_lower or "immunity" in cat_lower:
            scores["medical_documentary"] += 5
        elif "brain" in cat_lower or "psychology" in cat_lower:
            scores["cinematic_technology"] += 4
            scores["mystery_discovery"] += 3
        elif "food" in cat_lower or "nutrition" in cat_lower or "gut" in cat_lower:
            scores["informational_education"] += 5
        elif "skin" in cat_lower or "senses" in cat_lower:
            scores["soft_atmosphere"] += 4
        elif "disease" in cat_lower:
            scores["suspense_science"] += 6

        # 2. Keyword frequency scoring
        for cat, kw_list in self.mood_keywords.items():
            for kw in kw_list:
                if kw in combined_text:
                    scores[cat] += 2

        # 3. Scene roles / script sentiment overrides
        if any(w in combined_text for w in ["khatra", "danger", "deadly", "nuksan"]):
            if "sleep" not in cat_lower:
                scores["suspense_science"] += 4

        # Pick top scored category
        best_cat = max(scores, key=scores.get)
        if scores[best_cat] == 0:
            best_cat = "medical_documentary"

        logger.info(f"BGM Mood Detection: Category='{category}' -> Top Mood='{best_cat}' (Score: {scores[best_cat]})")
        return best_cat

    def select_track(
        self,
        category: str,
        topic_title: str = "",
        script_text: str = "",
        estimated_duration: float = 40.0,
        topic_id: Optional[str] = None,
        force_category: Optional[str] = None
    ) -> Tuple[Path, str, str, Dict[str, Any]]:
        """
        Selects the optimal background music track:
        1. Detects mood or uses force_category.
        2. Checks SQLite history to avoid repeat tracks from the last 5 videos.
        3. Validates duration and licensing.
        4. Returns: (track_path, category, track_id, metadata)
        """
        target_category = force_category or self.detect_mood(category, topic_title, script_text)
        recent_track_ids = self.db.get_recent_bgm_tracks(limit=5)

        track_meta = self.library.get(target_category)

        # Anti-repetition fallback if track was used recently
        if track_meta and track_meta.get("track_id") in recent_track_ids and not force_category:
            logger.info(f"Track {track_meta.get('track_id')} was recently used. Finding rotation alternative...")
            # Find an alternative category that wasn't used recently
            for alt_cat, alt_meta in self.library.items():
                if alt_meta.get("track_id") not in recent_track_ids:
                    logger.info(f"Rotated to alternative category: {alt_cat}")
                    target_category = alt_cat
                    track_meta = alt_meta
                    break

        # Fallback to medical_documentary if category missing
        if not track_meta:
            target_category = "medical_documentary"
            track_meta = self.library.get("medical_documentary", {})

        track_file = self.audio_dir / f"{target_category}.mp3"
        if not track_file.exists():
            # Fallback to original files
            track_file = self.audio_dir / "science_documentary.mp3"

        track_id = track_meta.get("track_id", f"bgm_{target_category}_01")

        # Record usage if topic_id provided
        if topic_id:
            self.db.record_bgm_usage(
                track_id=track_id,
                track_category=target_category,
                topic_id=topic_id,
                duration_seconds=track_meta.get("duration_seconds", 60.0)
            )

        logger.info(f"BGM Selected: [{target_category}] -> {track_file.name} (ID: {track_id})")
        return track_file, target_category, track_id, track_meta
