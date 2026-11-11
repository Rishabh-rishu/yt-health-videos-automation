"""
Medical Visual Graphics & Title Overlay Generator (V3 Clean Documentary Upgrade)
Completely eliminates decorative sci-fi HUD clutter (tiny labels, radar rings, ECG waveforms).
Features:
- Subtle cinematic gradient vignettes for 100% text contrast against bright or dark footage
- High-impact 0-3s Hook Title Card (via TitleEngine)
- Clean, bold documentary section headlines (via TitleEngine)
- Pure clean visuals on narrative scenes with zero UI obstruction
"""

from pathlib import Path
from PIL import Image, ImageDraw
import logging
from typing import Optional, List

from config.settings import VIDEO_WIDTH, VIDEO_HEIGHT
from visual.title_engine import TitleEngine

logger = logging.getLogger("health_videos.medical_hud")

class MedicalHUDGenerator:
    def __init__(self):
        self.title_engine = TitleEngine()

    def generate_hud_overlay(
        self,
        main_title: str,
        category: str,
        output_path: Path,
        concept_badge: Optional[str] = None,
        statistic: Optional[str] = None,
        is_hook_scene: bool = False,
        hook_text: Optional[str] = None,
        highlight_words: Optional[List[str]] = None
    ) -> Path:
        """
        Creates a clean 1080x1920 RGBA transparent overlay image.
        Netflix documentary standard: bold typography, high contrast, zero HUD clutter.
        """
        output_path.parent.mkdir(parents=True, exist_ok=True)
        img = Image.new("RGBA", (VIDEO_WIDTH, VIDEO_HEIGHT), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # 1. Subtle cinematic top & bottom gradient for perfect contrast
        # Top gradient: 0 to 240px
        for y in range(0, 240, 2):
            alpha = int(90 * (1.0 - (y / 240.0)))
            draw.line([(0, y), (VIDEO_WIDTH, y)], fill=(0, 0, 0, alpha))
            draw.line([(0, y + 1), (VIDEO_WIDTH, y + 1)], fill=(0, 0, 0, alpha))

        # Bottom gradient: 1400px to 1920px (behind subtitles)
        for y in range(1400, VIDEO_HEIGHT, 2):
            progress = (y - 1400) / (VIDEO_HEIGHT - 1400)
            alpha = int(120 * progress)
            draw.line([(0, y), (VIDEO_WIDTH, y)], fill=(0, 0, 0, alpha))
            draw.line([(0, y + 1), (VIDEO_WIDTH, y + 1)], fill=(0, 0, 0, alpha))

        # 2. Render Typography (Hook or Section)
        if is_hook_scene and hook_text:
            # 0-3s High-Impact Hook Question Card
            self.title_engine.render_hook_card(
                draw=draw,
                hook_text=hook_text,
                highlight_words=highlight_words,
                center_y=540
            )
        elif main_title and main_title != "MEDICAL SCAN":
            # Section headline for key scientific mechanisms
            self.title_engine.render_section_card(
                draw=draw,
                main_title=main_title,
                concept_badge=concept_badge,
                statistic=statistic,
                center_y=460
            )

        img.save(output_path, "PNG")
        return output_path
