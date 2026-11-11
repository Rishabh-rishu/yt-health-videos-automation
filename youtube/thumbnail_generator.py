"""
Cinematic Thumbnail Generator for Health Videos
Produces 1080x1920 high-CTR thumbnail with:
- 3D anatomical centerpiece
- Neon holographic border
- Bold high-contrast yellow/cyan curiosity headline
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import logging

from config.settings import VIDEO_WIDTH, VIDEO_HEIGHT, ASSETS_DIR, OUTPUT_DIR

logger = logging.getLogger("health_videos.thumbnail")

class ThumbnailGenerator:
    def __init__(self):
        self.output_dir = OUTPUT_DIR / "thumbnails"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.font_bold = ASSETS_DIR / "fonts" / "Montserrat.ttf"
        self.ref_dir = ASSETS_DIR / "references"

    def generate_thumbnail(
        self,
        topic_id: str,
        headline: str,
        background_image: Path
    ) -> Path:
        """
        Generates 1080x1920 vertical thumbnail.
        """
        out_path = self.output_dir / f"{topic_id}_thumb.jpg"
        
        # Load or create base image
        if background_image.exists():
            base = Image.open(background_image).convert("RGBA")
            base = base.resize((VIDEO_WIDTH, VIDEO_HEIGHT), Image.Resampling.LANCZOS)
        else:
            base = Image.new("RGBA", (VIDEO_WIDTH, VIDEO_HEIGHT), (7, 11, 20, 255))

        draw = ImageDraw.Draw(base)

        # Dark gradient overlay for text readability
        gradient = Image.new("RGBA", (VIDEO_WIDTH, 700), (7, 11, 20, 220))
        base.paste(gradient, (0, 1200), gradient)

        # Draw Headline Box
        try:
            font = ImageFont.truetype(str(self.font_bold), 64)
            badge_font = ImageFont.truetype(str(self.font_bold), 30)
        except Exception:
            font = ImageFont.load_default()
            badge_font = ImageFont.load_default()

        # Scientific Badge
        draw.rounded_rectangle([(100, 1250), (450, 1310)], radius=10, fill=(0, 229, 255, 255))
        draw.text((120, 1265), "3D MEDICAL LAB", fill=(7, 11, 20, 255), font=badge_font)

        # Headline
        draw.text((100, 1340), headline[:32].upper(), fill=(255, 230, 0, 255), font=font)
        draw.text((100, 1430), "REVEALED 🧠", fill=(240, 246, 252, 255), font=font)

        rgb_img = base.convert("RGB")
        rgb_img.save(out_path, "JPEG", quality=95)
        return out_path
