"""
Edge-TTS Female Voice Narration Provider (V2 Upgrade)
Generates studio-grade documentary narration using Microsoft Neural Female Voices.
Strictly enforces:
- Female voices ONLY (hi-IN-SwaraNeural / en-IN-NeerjaExpressiveNeural)
- Playback speed EXACTLY 1.15x (rate="+15%")
- Natural prosody optimization (micro-pause breathing injection & -1Hz pitch warmth)
- Full sentence boundary timecode extraction for sentence-to-visual synchronization
- Word-level timing calculation for animated subtitles
"""

import asyncio
import os
import re
import json
import logging
from pathlib import Path
from typing import List, Dict, Any, Tuple
import edge_tts

from config.settings import (
    DEFAULT_VOICE,
    VOICE_SPEED,
    VOICE_RATE_STR,
    FEMALE_VOICE_ONLY
)

logger = logging.getLogger("health_videos.voice.edge_tts")

ALLOWED_FEMALE_VOICES = {
    "hi-IN-SwaraNeural": "Hindi Female (Natural, Authoritative, Warm)",
    "en-IN-NeerjaExpressiveNeural": "Indian English/Hinglish Female (Expressive, Warm)",
    "en-IN-NeerjaNeural": "Indian English Female (Clear, Informative)"
}

class EdgeTTSFemaleProvider:
    def __init__(self, voice: str = DEFAULT_VOICE, speed: float = VOICE_SPEED, pitch: str = "-1Hz"):
        if FEMALE_VOICE_ONLY and voice not in ALLOWED_FEMALE_VOICES:
            logger.warning(f"Voice {voice} not in verified female list! Defaulting to hi-IN-SwaraNeural.")
            voice = "hi-IN-SwaraNeural"
        self.voice = voice
        self.speed = speed
        self.pitch = pitch
        self.rate_str = f"+{int(round((speed - 1.0) * 100))}%" if speed >= 1.0 else f"{int(round((speed - 1.0) * 100))}%"

    def optimize_prosody(self, text: str) -> str:
        """
        Injects natural breathing pauses and smooths Hinglish clause transitions.
        Eliminates the robotic monotone delivery by guiding neural pitch inflection.
        """
        t = text.strip()
        # Add micro-pause after introductory hooks and questions
        t = re.sub(r'^(Jab aap|Sote waqt|Kya aap|Kabhi socha hai|Har roz)\b', r'\1...', t, flags=re.IGNORECASE)
        t = re.sub(r'\?\s*', r'? ... ', t)
        # Ensure commas before coordinating conjunctions for natural breath
        t = re.sub(r'\s+(aur|lekin|jisse|parantu|isliye|taaki)\b', r', \1', t, flags=re.IGNORECASE)
        # Clean multiple punctuation
        t = re.sub(r'\.{4,}', '...', t)
        t = re.sub(r',\s*,', ',', t)
        return t

    async def generate_narration_async(
        self,
        text: str,
        output_audio_path: Path
    ) -> Tuple[bool, Path, List[Dict[str, Any]], List[Dict[str, Any]]]:
        """
        Synthesizes speech and extracts sentence and word-level timing boundaries.
        Returns: (success, audio_path, sentence_boundaries, word_boundaries)
        """
        output_audio_path.parent.mkdir(parents=True, exist_ok=True)
        prosody_text = self.optimize_prosody(text)
        
        comm = edge_tts.Communicate(
            text=prosody_text,
            voice=self.voice,
            rate=self.rate_str,
            pitch=self.pitch
        )

        sentence_boundaries = []
        audio_chunks = bytearray()

        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                audio_chunks.extend(chunk["data"])
            elif chunk["type"] == "SentenceBoundary":
                start_sec = chunk["offset"] / 10_000_000.0
                duration_sec = chunk["duration"] / 10_000_000.0
                end_sec = start_sec + duration_sec
                # Clean punctuation for clean subtitle display
                clean_sentence = chunk["text"].replace("...", " ").strip()
                sentence_boundaries.append({
                    "text": clean_sentence,
                    "start_sec": round(start_sec, 3),
                    "end_sec": round(end_sec, 3),
                    "duration_sec": round(duration_sec, 3)
                })

        with open(output_audio_path, "wb") as f:
            f.write(audio_chunks)

        # Word-level breakdown proportionally weighted by word character length
        word_boundaries = []
        for s_idx, s in enumerate(sentence_boundaries):
            words = [w for w in s["text"].strip().split() if w]
            if not words:
                continue
            s_start = s["start_sec"]
            s_dur = s["duration_sec"]
            total_chars = sum(len(w) for w in words)
            cur_w_start = s_start
            for w in words:
                w_dur = (len(w) / max(1, total_chars)) * s_dur
                w_end = cur_w_start + w_dur
                word_boundaries.append({
                    "word": w,
                    "start_sec": round(cur_w_start, 3),
                    "end_sec": round(w_end, 3),
                    "sentence_idx": s_idx
                })
                cur_w_start += w_dur

        logger.info(f"Generated prosody-enhanced female narration: {len(sentence_boundaries)} sentences, {len(word_boundaries)} words -> {output_audio_path}")
        return True, output_audio_path, sentence_boundaries, word_boundaries

    def generate_narration(
        self,
        text: str,
        output_audio_path: Path
    ) -> Tuple[bool, Path, List[Dict[str, Any]], List[Dict[str, Any]]]:
        return asyncio.run(self.generate_narration_async(text, output_audio_path))
