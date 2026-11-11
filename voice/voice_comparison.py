#!/usr/bin/env python3
"""
Female Voice Candidate Evaluation Benchmark (V3 Upgrade)
Generates side-by-side test samples across 3 female Indian voices and 3 distinct delivery styles:
1. Conversational Hinglish
2. Cinematic Documentary
3. Curious & Energetic Hook Delivery
Saves mastered comparison files to output/voice_candidates/ for user audition.
"""

import sys
import os
import asyncio
from pathlib import Path

# Add project root to sys.path
ROOT_PATH = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_PATH))

import edge_tts
import subprocess

from config.settings import OUTPUT_DIR, VOICE_SPEED, VOICE_RATE_STR

CANDIDATE_VOICES = {
    "swara_hindi": {
        "voice_id": "hi-IN-SwaraNeural",
        "description": "Swara (Hindi Female - Warm, Authoritative, Native Cadence)",
        "pitch": "-1Hz"
    },
    "neerja_expressive": {
        "voice_id": "en-IN-NeerjaExpressiveNeural",
        "description": "Neerja Expressive (Indian English/Hinglish - Dynamic, Engaging)",
        "pitch": "-0Hz"
    },
    "neerja_standard": {
        "voice_id": "en-IN-NeerjaNeural",
        "description": "Neerja Standard (Indian English - Clear, Informational Documentary)",
        "pitch": "-0Hz"
    }
}

TEST_SCRIPTS = {
    "1_hook_curious": (
        "Kya aapko pata hai? ... Sote waqt bhi aapka dimag ek extraordinary kaam karta hai! "
        "Aap so rahe hote hain, lekin aapka brain bilkul active rehta hai."
    ),
    "2_conversational": (
        "Jab aap gehri neend mein hote hain, aapke brain cells lagbhag sixty percent shrink ho jaate hain... "
        "jisse cerebrospinal fluid teji se flow karta hai aur din bhar ka toxic waste flush out kar deta hai."
    ),
    "3_documentary": (
        "Isse science mein Glymphatic System kehte hain. "
        "Yeh microscopic cleaning process aapke cognitive health aur memory ko protect karta hai. "
        "Toh aaj raat aap kitne ghante sone wale hain?"
    )
}

def apply_audio_mastering(input_mp3: Path, output_mp3: Path):
    """Applies broadcast audio mastering chain: 80Hz rumble removal, presence EQ, compression, -14 LUFS norm."""
    cmd = [
        "ffmpeg", "-y",
        "-i", str(input_mp3),
        "-af", (
            "highpass=f=80,"
            "equalizer=f=250:t=q:w=1.0:g=1.5,"
            "equalizer=f=3200:t=q:w=1.2:g=2.5,"
            "compand=attacks=0.02:decays=0.2:points=-80/-80|-40/-30|-20/-14|0/-2:gain=1.0,"
            "loudnorm=I=-14:TP=-1.0:LRA=7"
        ),
        "-c:a", "libmp3lame",
        "-b:a", "192k",
        str(output_mp3)
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

async def generate_samples():
    out_dir = OUTPUT_DIR / "voice_candidates"
    out_dir.mkdir(parents=True, exist_ok=True)
    temp_dir = out_dir / "raw"
    temp_dir.mkdir(parents=True, exist_ok=True)

    print("\n" + "=" * 65)
    print("  HEALTH VIDEOS V3 — FEMALE VOICE BENCHMARK EVALUATION")
    print("=" * 65)
    print(f"Narration Speed: {VOICE_SPEED}x ({VOICE_RATE_STR})")
    print(f"Output Directory: {out_dir.resolve()}\n")

    results = []

    for c_key, c_info in CANDIDATE_VOICES.items():
        v_id = c_info["voice_id"]
        v_desc = c_info["description"]
        v_pitch = c_info["pitch"]
        print(f"▶ Synthesizing Voice: {v_id} ({v_desc})")

        for s_style, s_text in TEST_SCRIPTS.items():
            raw_path = temp_dir / f"{c_key}_{s_style}_raw.mp3"
            master_path = out_dir / f"{c_key}_{s_style}.mp3"

            comm = edge_tts.Communicate(
                text=s_text,
                voice=v_id,
                rate=VOICE_RATE_STR,
                pitch=v_pitch
            )
            await comm.save(str(raw_path))

            # Apply broadcast mastering chain
            apply_audio_mastering(raw_path, master_path)

            dur_cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(master_path)]
            dur = float(subprocess.check_output(dur_cmd).strip())

            results.append({
                "voice": v_id,
                "style": s_style,
                "duration": round(dur, 2),
                "file": str(master_path)
            })
            print(f"   ✓ {s_style}: {dur:.2f}s -> {master_path.name}")

    print("\n" + "=" * 65)
    print("  BENCHMARK COMPLETED SUCCESSFULLY!")
    print("=" * 65 + "\n")
    return results

if __name__ == "__main__":
    asyncio.run(generate_samples())
