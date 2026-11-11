"""
Visual Branding & Identity System for Health Videos Channel
Grounded in the 7 reference photos:
- Photorealistic 3D holographic human anatomy
- Medical HUD diagnostics & telemetry
- Microscopic cellular environments
- Word-level yellow/cyan dynamic subtitles
"""

from dataclasses import dataclass
from typing import Dict, Any

@dataclass(frozen=True)
class ColorPalette:
    BACKGROUND_DARK = "#070B14"       # Deep dark slate / midnight navy
    BACKGROUND_CARD = "#0D1524"       # Translucent HUD panel background
    CYAN_HOLO = "#00E5FF"             # 3D holographic outline & neuron tendrils
    TEAL_BIO = "#00FFA3"              # Microscopic pathogen / biological glow
    RED_ARTERIAL = "#FF2E56"          # Arterial blood flow & cardiovascular focus
    BLUE_VENOUS = "#1E88E5"           # Venous return & oxygen-depleted blood
    GOLD_SYNAPSE = "#FFB300"          # Brain electrical impulses & energy bursts
    WHITE_IVORY = "#F0F6FC"           # Clean skeletal bone & clinical typography
    HIGHLIGHT_YELLOW = "#FFE600"      # Active word-level subtitle highlight
    HIGHLIGHT_CYAN = "#00E5FF"        # Scientific keyword subtitle highlight
    BORDER_HUD = "rgba(0, 229, 255, 0.35)" # HUD panel outline
    HUD_GLOW = "0 0 15px rgba(0, 229, 255, 0.45)"

CHANNEL_NAME = "Health Science"
CHANNEL_TAGLINE = "Human Body & Medical Science"
CHANNEL_WATERMARK = "HEALTH LAB"

# Subtitle typography specifications
SUBTITLE_STYLE = {
    "font_family": "Mukta, Montserrat, sans-serif",
    "font_size": 48,
    "font_weight": "800",
    "text_color": "#FFFFFF",
    "stroke_color": "#000000",
    "stroke_width": 4,
    "highlight_color": ColorPalette.HIGHLIGHT_YELLOW,
    "alt_highlight_color": ColorPalette.HIGHLIGHT_CYAN,
    "bottom_margin": 480,  # Above YouTube Shorts description and controls
    "max_words_per_line": 4
}

# Category-specific theme mapping
CATEGORY_THEMES: Dict[str, Dict[str, str]] = {
    "Brain and Psychology": {
        "primary": ColorPalette.CYAN_HOLO,
        "secondary": ColorPalette.GOLD_SYNAPSE,
        "accent": "#9C27B0",
        "icon": "🧠",
        "bgm": "ancient_mystery_ambience.mp3"
    },
    "Sleep Science": {
        "primary": ColorPalette.CYAN_HOLO,
        "secondary": "#7C4DFF",
        "accent": ColorPalette.GOLD_SYNAPSE,
        "icon": "💤",
        "bgm": "space_atmosphere.mp3"
    },
    "Heart and Blood Circulation": {
        "primary": ColorPalette.RED_ARTERIAL,
        "secondary": ColorPalette.BLUE_VENOUS,
        "accent": ColorPalette.GOLD_SYNAPSE,
        "icon": "🫀",
        "bgm": "science_documentary.mp3"
    },
    "Immunity and Microbiology": {
        "primary": ColorPalette.TEAL_BIO,
        "secondary": ColorPalette.RED_ARTERIAL,
        "accent": ColorPalette.CYAN_HOLO,
        "icon": "🔬",
        "bgm": "dark_cinematic_suspense.mp3"
    },
    "Food and Nutrition": {
        "primary": "#4CAF50",
        "secondary": ColorPalette.GOLD_SYNAPSE,
        "accent": ColorPalette.RED_ARTERIAL,
        "icon": "🥗",
        "bgm": "nature_documentary.mp3"
    },
    "Fitness and Muscle Science": {
        "primary": ColorPalette.GOLD_SYNAPSE,
        "secondary": ColorPalette.RED_ARTERIAL,
        "accent": ColorPalette.CYAN_HOLO,
        "icon": "⚡",
        "bgm": "epic_historical_storytelling.mp3"
    }
}
