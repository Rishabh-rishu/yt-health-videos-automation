"""
Medical HUD (Heads-Up Display) Graphics Generator (V2)
Generates holographic sci-fi medical diagnostic overlays:
- Top Telemetry Bar (Live Bio-Scan status & system category)
- Circular diagnostic dials & anatomical scan radar
- Multi-tiered broadcast title cards via TitleEngine
- Animated ECG vital waveform
Grounded directly in Reference Image 1 & 7.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math
import logging
from typing import Optional

from config.settings import VIDEO_WIDTH, VIDEO_HEIGHT, ASSETS_DIR
from visual.title_engine import TitleEngine

logger = logging.getLogger("health_videos.medical_hud")

class MedicalHUDGenerator:
    def __init__(self):
        self.hud_dir = ASSETS_DIR / "hud_elements"
        self.hud_dir.mkdir(parents=True, exist_ok=True)
        self.font_path = ASSETS_DIR / "fonts" / "Montserrat.ttf"
        self.title_engine = TitleEngine()

    def generate_hud_overlay(
        self,
        main_title: str,
        category: str,
        output_path: Path,
        concept_badge: Optional[str] = None,
        statistic: Optional[str] = None
    ) -> Path:
        """
        Creates a 1080x1920 RGBA transparent HUD overlay image.
        Features diagnostic radar dials, ECG vital wave, and glowing title card.
        """
        output_path.parent.mkdir(parents=True, exist_ok=True)
        img = Image.new("RGBA", (VIDEO_WIDTH, VIDEO_HEIGHT), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        try:
            font_sm = ImageFont.truetype(str(self.font_path), 22)
        except Exception:
            font_sm = ImageFont.load_default()

        # 1. Top HUD Header Bar
        # Live Bio-Scan Badge
        draw.rounded_rectangle([(60, 100), (380, 150)], radius=8, outline=(0, 229, 255, 180), width=2, fill=(7, 11, 20, 160))
        draw.text((80, 114), "● LIVE BIO-SCAN: ACTIVE", fill=(0, 229, 255, 240), font=font_sm)

        # Right Telemetry Counter
        cat_tag = category[:14].upper()
        draw.rounded_rectangle([(700, 100), (1020, 150)], radius=8, outline=(0, 229, 255, 120), width=1, fill=(7, 11, 20, 140))
        draw.text((720, 114), f"SYS: {cat_tag}", fill=(240, 246, 252, 220), font=font_sm)

        # 2. Side Circular Diagnostic Dial (Reference Image 1)
        cx, cy, r = 960, 360, 60
        draw.ellipse([(cx - r, cy - r), (cx + r, cy + r)], outline=(0, 229, 255, 140), width=2)
        draw.ellipse([(cx - r + 15, cy - r + 15), (cx + r - 15, cy + r - 15)], outline=(0, 255, 163, 100), width=1)
        for angle in range(0, 360, 30):
            rad = math.radians(angle)
            x1 = cx + (r - 10) * math.cos(rad)
            y1 = cy + (r - 10) * math.sin(rad)
            x2 = cx + r * math.cos(rad)
            y2 = cy + r * math.sin(rad)
            draw.line([(x1, y1), (x2, y2)], fill=(0, 229, 255, 160), width=1)

        # 3. Multi-Tiered Title Card
        if main_title:
            self.title_engine.render_title_card(
                draw=draw,
                main_title=main_title,
                concept_badge=concept_badge,
                statistic=statistic,
                center_y=1260
            )

        # 4. ECG Vital Rhythm Waveform along bottom (above subtitles)
        wave_y = 1380
        points = []
        for x in range(60, 1020, 12):
            if 480 <= x <= 560:
                y_offset = -35 if x == 520 else (20 if x in (500, 540) else 0)
            else:
                y_offset = int(math.sin(x / 40.0) * 6)
            points.append((x, wave_y + y_offset))
        if len(points) > 1:
            draw.line(points, fill=(0, 255, 163, 140), width=2)

        img.save(output_path, "PNG")
        return output_path
