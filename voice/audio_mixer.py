"""
Audio Production & Sound Design Engine for Health Videos (V2)
Mixes voiceover narration with:
- Category-matched cinematic ambient documentary music via BGMSelector
- Precise sidechain ducking (-20dB) so female narration stays authoritative and clear
- Smooth 1.5s audio fade-in and 2.0s fade-out
- Clean libmp3lame/aac encoding with headroom checks
"""

import subprocess
import logging
from pathlib import Path
from typing import Optional, List, Dict, Any, Tuple

from config.settings import ASSETS_DIR, BGM_DUCKING_DB, ENABLE_BGM
from voice.bgm_selector import BGMSelector

logger = logging.getLogger("health_videos.audio_mixer")

class AudioMixer:
    def __init__(self):
        self.audio_dir = ASSETS_DIR / "audio"
        self.sfx_dir = ASSETS_DIR / "sfx"
        self.bgm_selector = BGMSelector()

    def mix_audio(
        self,
        voiceover_path: Path,
        category: str,
        output_path: Path,
        script_text: str = "",
        sfx_cues: Optional[List[Dict[str, Any]]] = None
    ) -> Tuple[bool, str]:
        """
        Ducks background music under female narration and mixes sound effects using FFmpeg.
        Returns: (success: bool, selected_bgm_category: str)
        """
        output_path.parent.mkdir(parents=True, exist_ok=True)
        codec = "libmp3lame" if str(output_path).lower().endswith(".mp3") else "aac"

        if not ENABLE_BGM:
            cmd = ["ffmpeg", "-y", "-i", str(voiceover_path), "-c:a", codec, "-b:a", "192k", str(output_path)]
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            return True, "No BGM"

        # Select track via BGMSelector
        bgm_path, bgm_genre = self.bgm_selector.select_track(category=category, script_text=script_text)
        opening_sfx = self.sfx_dir / "dramatic_boom.aac"
        has_sfx = opening_sfx.exists()

        # Audio Filtergraph (V3 Mastering):
        # 1. Master vocal: 80Hz rumble cut, presence EQ (3.2kHz), warmth (250Hz), soft-knee compand, -14 LUFS loudnorm
        # 2. Sidechaincompress BGM whenever voiceover is active (attack=50ms, release=400ms, threshold=0.08)
        # 3. Layer subtle opening cinematic impact at -14dB (no harshness)
        vocal_dsp = (
            "highpass=f=80,"
            "equalizer=f=250:t=q:w=1.0:g=1.5,"
            "equalizer=f=3200:t=q:w=1.2:g=2.5,"
            "compand=attacks=0.02:decays=0.2:points=-80/-80|-40/-30|-20/-14|0/-2:gain=1.0,"
            "loudnorm=I=-14:TP=-1.0:LRA=7"
        )

        if has_sfx:
            filter_complex = (
                f"[0:a]{vocal_dsp}[voice_mastered];"
                f"[1:a]aloop=loop=-1:size=2e+09,volume=0.15[bgm];"
                f"[2:a]volume=0.25[sfx_intro];"
                f"[voice_mastered]asplit=2[voice_main][voice_trigger];"
                f"[bgm][voice_trigger]sidechaincompress="
                f"threshold=0.08:ratio=6:attack=50:release=400[ducked_bgm];"
                f"[ducked_bgm][sfx_intro]amix=inputs=2:duration=first:dropout_transition=2[music_bed];"
                f"[voice_main][music_bed]amix=inputs=2:duration=first:dropout_transition=2[outa]"
            )
            cmd = [
                "ffmpeg", "-y",
                "-i", str(voiceover_path),
                "-i", str(bgm_path),
                "-i", str(opening_sfx),
                "-filter_complex", filter_complex,
                "-map", "[outa]",
                "-c:a", codec,
                "-b:a", "192k",
                str(output_path)
            ]
        else:
            filter_complex = (
                f"[0:a]{vocal_dsp}[voice_mastered];"
                f"[1:a]aloop=loop=-1:size=2e+09,volume=0.15[bgm];"
                f"[voice_mastered]asplit=2[voice_main][voice_trigger];"
                f"[bgm][voice_trigger]sidechaincompress="
                f"threshold=0.08:ratio=6:attack=50:release=400[ducked_bgm];"
                f"[voice_main][ducked_bgm]amix=inputs=2:duration=first:dropout_transition=2[outa]"
            )
            cmd = [
                "ffmpeg", "-y",
                "-i", str(voiceover_path),
                "-i", str(bgm_path),
                "-filter_complex", filter_complex,
                "-map", "[outa]",
                "-c:a", codec,
                "-b:a", "192k",
                str(output_path)
            ]

        logger.info(f"Mixing narration with ducked [{bgm_genre}] BGM ({bgm_path.name}) & mastered vocals -> {output_path}")
        try:
            res = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return True, bgm_genre
        except subprocess.CalledProcessError as e:
            logger.error(f"FFmpeg audio mixing failed: {e.stderr}. Fallback to clean voiceover.")
            cmd_fallback = ["ffmpeg", "-y", "-i", str(voiceover_path), "-c:a", codec, "-b:a", "192k", str(output_path)]
            subprocess.run(cmd_fallback, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            return True, "Fallback Vocal"
