"""
Dynamic Subtitle Generator for Health Videos (V2 Upgrade)
Produces word-level and phrase-level synchronized subtitles with:
- 15% Increased typography size (62px base, 66px active word pop)
- Bold high-visibility typography (Mukta / Montserrat)
- Highlighted active words in electric yellow (#FFE600) with scale pop
- Heavily outlined with dark drop shadow (5px outline, 3px shadow)
- Strictly positioned in vertical YouTube Shorts safe zone (MarginV: 480px)
- Zero overlap with title cards or bottom platform UI controls
"""

import json
from pathlib import Path
from typing import List, Dict, Any

from config.settings import VIDEO_WIDTH, VIDEO_HEIGHT, SAFE_ZONE_BOTTOM
from config.branding import SUBTITLE_STYLE, ColorPalette

class SubtitleGenerator:
    def __init__(self):
        self.style = SUBTITLE_STYLE

    def generate_ass_subtitles(
        self,
        word_boundaries: List[Dict[str, Any]],
        output_ass_path: Path
    ) -> Path:
        """
        Generates Advanced SubStation Alpha (.ass) subtitle file with word-level pop highlights.
        Font size increased by ~15% for optimal mobile readability.
        """
        output_ass_path.parent.mkdir(parents=True, exist_ok=True)
        
        # ASS Header with 70px base / 76px highlight font size (V3 Upgrade)
        safe_v = 440
        ass_content = f"""[Script Info]
Title: Health Videos Dynamic Subtitles V3
ScriptType: v4.00+
WrapStyle: 0
PlayResX: {VIDEO_WIDTH}
PlayResY: {VIDEO_HEIGHT}
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Mukta,70,&H00FFFFFF,&H0000E6FF,&H00000000,&HA0000000,-1,0,0,0,100,100,0,0,1,6,4,2,60,60,{safe_v},1
Style: Highlight,Mukta,76,&H0000E6FF,&H00FFFFFF,&H00000000,&HC0000000,-1,0,0,0,112,112,0,0,1,7,4,2,60,60,{safe_v},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
        # Group words into short 3-4 word punchy phrases
        chunks = []
        chunk_size = 4
        for i in range(0, len(word_boundaries), chunk_size):
            group = word_boundaries[i:i + chunk_size]
            if not group:
                continue
            start_sec = group[0]["start_sec"]
            end_sec = group[-1]["end_sec"]
            chunks.append({
                "words": group,
                "start": start_sec,
                "end": end_sec
            })

        for chunk in chunks:
            for w_idx, active_w in enumerate(chunk["words"]):
                w_start = active_w["start_sec"]
                w_end = active_w["end_sec"]

                # Build phrase text with active word highlighted in Electric Yellow with subtle scale pop
                text_parts = []
                for w in chunk["words"]:
                    if w["word"] == active_w["word"] and w["start_sec"] == active_w["start_sec"]:
                        # Active word: Electric Yellow & 112% pop scaled
                        text_parts.append(r"{\c&H0000E6FF\b1\fscx112\fscy112}" + w["word"] + r"{\r}")
                    else:
                        # Inactive words: Crisp White & standard scale
                        text_parts.append(r"{\c&H00FFFFFF\b1\fscx100\fscy100}" + w["word"] + r"{\r}")

                line_text = " ".join(text_parts)
                start_fmt = self._format_timestamp(w_start)
                end_fmt = self._format_timestamp(w_end)
                ass_content += f"Dialogue: 0,{start_fmt},{end_fmt},Default,,0,0,0,,{line_text}\n"

        with open(output_ass_path, "w", encoding="utf-8") as f:
            f.write(ass_content)

        return output_ass_path

    def _format_timestamp(self, seconds: float) -> str:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        centis = int(round((seconds - int(seconds)) * 100))
        return f"{hours:d}:{minutes:02d}:{secs:02d}.{centis:02d}"
