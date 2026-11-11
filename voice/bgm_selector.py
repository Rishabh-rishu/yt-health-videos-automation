"""
Dynamic Background Music Selector & Tone Classifier for Health Videos (V2)
Maps medical topics and narration scripts to 5 distinct documentary moods:
1. Suspense / Mystery (ancient_mystery_ambience.mp3)
2. Medical / Science (science_documentary.mp3)
3. Informational / Educational (nature_documentary.mp3)
4. Emotional / Human Body (space_atmosphere.mp3)
5. Warning / Risk Awareness (dark_cinematic_suspense.mp3)
"""

import json
import logging
from pathlib import Path
from typing import Tuple, Dict, Any

from config.settings import ASSETS_DIR

logger = logging.getLogger("health_videos.bgm_selector")

class BGMSelector:
    def __init__(self):
        self.audio_dir = ASSETS_DIR / "audio"
        self.tracks = {
            "Suspense / Mystery": {
                "file": "ancient_mystery_ambience.mp3",
                "desc": "Subtle tension, deep atmospheric pads, soft pulses.",
                "keywords": ["mystery", "secret", "hidden", "unknown", "wonder", "why"]
            },
            "Medical / Science": {
                "file": "science_documentary.mp3",
                "desc": "Futuristic ambient textures, clean electronic atmosphere, subtle pulses.",
                "keywords": ["heart", "circulation", "blood", "artery", "cardiac", "microbiology", "cell"]
            },
            "Informational / Educational": {
                "file": "nature_documentary.mp3",
                "desc": "Light rhythmic background, positive and engaging, calm but not boring.",
                "keywords": ["food", "nutrition", "diet", "habit", "water", "vitamins", "fitness"]
            },
            "Emotional / Human Body": {
                "file": "space_atmosphere.mp3",
                "desc": "Soft atmospheric pads, recovery, sleep, calming neural rejuvenation.",
                "keywords": ["sleep", "brain", "rest", "glymphatic", "peaceful", "recovery", "dream"]
            },
            "Warning / Risk Awareness": {
                "file": "dark_cinematic_suspense.mp3",
                "desc": "Controlled tension, serious documentary atmosphere, disease risk.",
                "keywords": ["disease", "risk", "danger", "toxin", "sugar", "damage", "decline", "warning"]
            }
        }

    def select_track(self, category: str, script_text: str = "") -> Tuple[Path, str]:
        """
        Selects the optimal documentary music bed based on category and script sentiment.
        Returns: (track_path, category_name)
        """
        cat_lower = category.lower()
        script_lower = script_text.lower()

        # Category-based primary mapping
        if "sleep" in cat_lower:
            selected_cat = "Emotional / Human Body"
        elif "brain" in cat_lower or "mystery" in cat_lower:
            selected_cat = "Suspense / Mystery"
        elif "heart" in cat_lower or "immunity" in cat_lower:
            selected_cat = "Medical / Science"
        elif "food" in cat_lower or "fitness" in cat_lower:
            selected_cat = "Informational / Educational"
        elif "disease" in cat_lower or "risk" in cat_lower:
            selected_cat = "Warning / Risk Awareness"
        else:
            selected_cat = "Medical / Science"

        # Check script text for strong warning/danger cues
        if any(w in script_lower for w in ["risk", "danger", "khatra", "nuksan", "disease"]):
            if "sleep" not in cat_lower: # Sleep videos remain soothing
                selected_cat = "Warning / Risk Awareness"

        track_info = self.tracks.get(selected_cat, self.tracks["Medical / Science"])
        track_path = self.audio_dir / track_info["file"]
        if not track_path.exists():
            track_path = self.audio_dir / "science_documentary.mp3"

        logger.info(f"BGM Selector: Selected [{selected_cat}] -> {track_path.name}")
        return track_path, selected_cat
