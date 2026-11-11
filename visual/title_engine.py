"""
Broadcast-Grade Medical Title & Typography Engine (V3 Upgrade)
Implements a Netflix-style science documentary typography system:
- Large, bold mobile-readable typography (Montserrat ExtraBold / Black)
- High-contrast text rendering with subtle dark pill plates
- Dedicated 0-3s Hook Title Card (74px bold font with yellow/cyan keyword highlights)
- Modern Section Mechanism Cards (64px bold font with clean category badges)
- Zero decorative sci-fi clutter or tiny illegible labels
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from typing import Tuple, List, Optional
import textwrap
import re

from config.settings import VIDEO_WIDTH, VIDEO_HEIGHT, ASSETS_DIR

class TitleEngine:
    def __init__(self):
        self.font_dir = ASSETS_DIR / "fonts"
        self._load_fonts()

    def _load_fonts(self):
        try:
            bold_font = self.font_dir / "Mukta-Bold.ttf"
            semibold_font = self.font_dir / "Mukta-SemiBold.ttf"

            if bold_font.exists():
                self.font_hook = ImageFont.truetype(str(bold_font), 72)
                self.font_section = ImageFont.truetype(str(bold_font), 62)
                self.font_stat = ImageFont.truetype(str(bold_font), 30)
            else:
                self.font_hook = ImageFont.load_default()
                self.font_section = ImageFont.load_default()
                self.font_stat = ImageFont.load_default()

            if semibold_font.exists():
                self.font_badge = ImageFont.truetype(str(semibold_font), 28)
            else:
                self.font_badge = ImageFont.load_default()
        except Exception:
            self.font_hook = ImageFont.load_default()
            self.font_section = ImageFont.load_default()
            self.font_badge = ImageFont.load_default()
            self.font_stat = ImageFont.load_default()

    def render_hook_card(
        self,
        draw: ImageDraw.ImageDraw,
        hook_text: str,
        highlight_words: Optional[List[str]] = None,
        center_y: int = 560
    ):
        """
        Renders a large, bold, high-contrast 0-3s Hook Question on mobile screen.
        Features electric yellow keyword highlights and dark translucent frosted backing.
        """
        if not hook_text:
            return

        clean_text = hook_text.strip()
        wrapped_lines = textwrap.wrap(clean_text, width=22)
        if len(wrapped_lines) > 3:
            wrapped_lines = textwrap.wrap(clean_text, width=26)

        line_height = 86
        text_block_h = len(wrapped_lines) * line_height
        
        # Determine container dimensions
        max_line_len = max(len(l) for l in wrapped_lines)
        card_w = min(1020, max(720, max_line_len * 42 + 100))
        card_h = text_block_h + 70
        card_x = (VIDEO_WIDTH - card_w) // 2
        card_y = center_y - (card_h // 2)

        # 1. Deep contrast frosted backing for 100% legibility on mobile
        draw.rounded_rectangle(
            [(card_x, card_y), (card_x + card_w, card_y + card_h)],
            radius=24,
            fill=(8, 12, 22, 235),
            outline=(0, 229, 255, 180),
            width=3
        )
        # Top glowing accent line
        draw.rounded_rectangle(
            [(card_x + 40, card_y), (card_x + card_w - 40, card_y + 4)],
            radius=2,
            fill=(0, 229, 255, 240)
        )

        # 2. Render each line with keyword highlighting
        hl_set = [w.lower().strip(",.?!") for w in (highlight_words or [])]
        curr_y = card_y + 30

        for line in wrapped_lines:
            words = line.split()
            # Calculate total width of the line to center it
            # We measure word by word
            line_parts = []
            total_w = 0
            space_w = draw.textlength(" ", font=self.font_hook)

            for w in words:
                w_clean = re.sub(r'[^a-zA-Z0-9\u0900-\u097F]', '', w).lower()
                is_hl = any(h == w_clean or h in w_clean for h in hl_set)
                w_len = draw.textlength(w, font=self.font_hook)
                line_parts.append((w, is_hl, w_len))
                total_w += w_len + space_w
            total_w -= space_w

            start_x = (VIDEO_WIDTH - total_w) // 2

            curr_x = start_x
            for w, is_hl, w_len in line_parts:
                color = (255, 230, 0, 255) if is_hl else (255, 255, 255, 255) # Electric yellow or crisp white
                # Drop shadow
                draw.text((curr_x + 3, curr_y + 3), w, fill=(0, 0, 0, 220), font=self.font_hook)
                draw.text((curr_x, curr_y), w, fill=color, font=self.font_hook)
                curr_x += w_len + space_w

            curr_y += line_height

    def render_section_card(
        self,
        draw: ImageDraw.ImageDraw,
        main_title: str,
        concept_badge: Optional[str] = None,
        statistic: Optional[str] = None,
        center_y: int = 500
    ):
        """
        Renders a clean, bold Netflix-style documentary section headline.
        """
        if not main_title:
            return

        clean_title = main_title.strip().upper()
        wrapped_lines = textwrap.wrap(clean_title, width=20)
        line_height = 68
        text_block_h = len(wrapped_lines) * line_height

        badge_h = 36 if concept_badge else 0
        stat_h = 36 if statistic else 0
        padding = 24

        total_card_h = text_block_h + badge_h + stat_h + (padding * 2)
        card_w = min(960, max(580, max(len(l) for l in wrapped_lines) * 34 + 80))
        card_x = (VIDEO_WIDTH - card_w) // 2
        card_y = center_y - (total_card_h // 2)

        # High-contrast dark glass plate
        draw.rounded_rectangle(
            [(card_x, card_y), (card_x + card_w, card_y + total_card_h)],
            radius=20,
            fill=(8, 12, 22, 235),
            outline=(0, 229, 255, 150),
            width=3
        )

        curr_y = card_y + padding

        # Concept Badge (e.g. ● GLYMPHATIC SYSTEM)
        if concept_badge:
            b_text = f"● {concept_badge.upper()}"
            draw.text((card_x + 38, curr_y), b_text, fill=(0, 255, 163, 255), font=self.font_badge)
            curr_y += badge_h + 4

        # Main Title (e.g. BRAIN CLEANUP / CSF FLUID FLUSH)
        for line in wrapped_lines:
            draw.text((card_x + 40, curr_y + 3), line, fill=(0, 0, 0, 240), font=self.font_section)
            draw.text((card_x + 38, curr_y), line, fill=(255, 255, 255, 255), font=self.font_section)
            curr_y += line_height

        # Highlight Metric / Statistic (e.g. 60% EXPANSION)
        if statistic:
            curr_y += 6
            stat_text = statistic.upper()
            stat_w = int(draw.textlength(stat_text, font=self.font_stat)) + 30
            draw.rounded_rectangle(
                [(card_x + 36, curr_y), (card_x + 36 + stat_w, curr_y + 38)],
                radius=8,
                fill=(255, 230, 0, 255)
            )
            draw.text((card_x + 51, curr_y + 4), stat_text, fill=(6, 9, 16, 255), font=self.font_stat)
