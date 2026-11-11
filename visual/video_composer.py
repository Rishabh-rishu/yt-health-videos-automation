"""
Master Video Compositor Engine for Health Videos
Coordinates multi-layer video synthesis:
- Layer 1: Contextual 3D anatomical and microscopic video clips (cropped to 1080x1920 9:16)
- Layer 2: Transparent Medical HUD overlay with telemetry dials, radar, and ECG pulse
- Layer 3: Word-level animated yellow/cyan highlighted subtitles in Shorts safe zone
- Layer 4: Final color grading LUT (cinematic high-contrast medical documentary grade)
- Audio: Ducked female narration (1.15x) + science documentary ambient BGM
"""

import subprocess
import logging
from pathlib import Path
from typing import List, Dict, Any, Tuple

from config.settings import (
    VIDEO_WIDTH,
    VIDEO_HEIGHT,
    VIDEO_FPS,
    OUTPUT_DIR,
    ASSETS_DIR
)

logger = logging.getLogger("health_videos.video_composer")

class VideoComposer:
    def __init__(self):
        self.output_dir = OUTPUT_DIR / "videos"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.font_dir = ASSETS_DIR / "fonts"

    def compose_short(
        self,
        topic_id: str,
        scenes: List[Dict[str, Any]],
        mixed_audio_path: Path,
        ass_subtitles_path: Path,
        total_duration: float
    ) -> Tuple[bool, Path, str]:
        """
        Renders the final 1080x1920 30FPS vertical MP4 video using FFmpeg filter complex.
        """
        final_mp4 = self.output_dir / f"{topic_id}_health_short.mp4"
        temp_visual_mp4 = self.output_dir / f"{topic_id}_temp_visual.mp4"

        logger.info(f"Composing Short for {topic_id} ({len(scenes)} scenes, {total_duration:.2f}s)")

        # 1. Build video segment for each scene
        scene_segments = []
        for idx, scene in enumerate(scenes):
            asset_path = scene.get("asset_path")
            hud_path = scene.get("hud_overlay_path")
            dur = max(0.5, scene.get("duration_sec", 5.0))
            seg_path = self.output_dir / f"{topic_id}_seg_{idx:02d}.mp4"

            # Check if asset is video or image
            is_video = asset_path and asset_path.lower().endswith((".mp4", ".mov", ".webm"))

            if is_video and Path(asset_path).exists():
                vf = (
                    f"scale={VIDEO_WIDTH}:{VIDEO_HEIGHT}:force_original_aspect_ratio=increase,"
                    f"crop={VIDEO_WIDTH}:{VIDEO_HEIGHT},"
                    f"fps={VIDEO_FPS},"
                    f"format=yuv420p"
                )
                # Safely offset past stock footage black intro fades (e.g. 2.5s) if clip is sufficiently long
                seek_args = []
                try:
                    probe_cmd = [
                        "ffprobe", "-v", "error",
                        "-show_entries", "format=duration",
                        "-of", "default=noprint_wrappers=1:nokey=1",
                        str(asset_path)
                    ]
                    clip_dur = float(subprocess.check_output(probe_cmd).strip())
                    if clip_dur > 5.5:
                        seek_args = ["-ss", "2.8"]
                except Exception:
                    seek_args = []

                input_args = [*seek_args, "-stream_loop", "-1", "-i", str(asset_path)]
            else:
                zoom_expr = "zoom+0.0012" if idx % 2 == 0 else "if(eq(on,1),1.15,zoom-0.0012)"
                vf = (
                    f"scale={VIDEO_WIDTH}:{VIDEO_HEIGHT}:force_original_aspect_ratio=increase,"
                    f"crop={VIDEO_WIDTH}:{VIDEO_HEIGHT},"
                    f"zoompan=z='min(max({zoom_expr},1.0),1.25)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={int(dur * VIDEO_FPS)}:s={VIDEO_WIDTH}x{VIDEO_HEIGHT}:fps={VIDEO_FPS},"
                    f"format=yuv420p"
                )
                input_args = ["-loop", "1", "-i", str(asset_path) if asset_path else str(ASSETS_DIR / "references" / "media_1794379567781.png")]

            if hud_path and Path(hud_path).exists():
                seg_cmd = [
                    "ffmpeg", "-y",
                    *input_args,
                    "-i", str(hud_path),
                    "-filter_complex",
                    f"[0:v]{vf}[base];[base][1:v]overlay=0:0:format=auto[v_out]",
                    "-map", "[v_out]",
                    "-t", str(dur),
                    "-c:v", "libx264",
                    "-preset", "fast",
                    "-pix_fmt", "yuv420p",
                    str(seg_path)
                ]
            else:
                seg_cmd = [
                    "ffmpeg", "-y",
                    *input_args,
                    "-vf", vf,
                    "-t", str(dur),
                    "-c:v", "libx264",
                    "-preset", "fast",
                    "-pix_fmt", "yuv420p",
                    str(seg_path)
                ]

            try:
                subprocess.run(seg_cmd, capture_output=True, text=True, check=True)
                scene_segments.append(seg_path)
            except subprocess.CalledProcessError as e:
                logger.error(f"Error rendering segment {idx}: {e.stderr}")
                return False, final_mp4, f"Segment {idx} render failed: {e.stderr[:200]}"

        # 2. Concatenate all visual segments
        concat_txt = self.output_dir / f"{topic_id}_concat.txt"
        with open(concat_txt, "w") as f:
            for seg in scene_segments:
                f.write(f"file '{seg.resolve()}'\n")

        concat_cmd = [
            "ffmpeg", "-y",
            "-f", "concat",
            "-safe", "0",
            "-i", str(concat_txt),
            "-c", "copy",
            str(temp_visual_mp4)
        ]
        try:
            subprocess.run(concat_cmd, capture_output=True, text=True, check=True)
        except subprocess.CalledProcessError as e:
            return False, final_mp4, f"Concatenation failed: {e.stderr[:200]}"

        # 3. Burn in word-highlighted subtitles and merge with audio
        # Escape path for FFmpeg subtitles filter
        escaped_sub = str(ass_subtitles_path).replace(":", r"\:").replace("'", r"\'")
        escaped_fontdir = str(self.font_dir).replace(":", r"\:").replace("'", r"\'")
        
        color_grade = "eq=contrast=1.06:brightness=-0.02:saturation=1.12"
        sub_filter = f"subtitles='{escaped_sub}':fontsdir='{escaped_fontdir}'"
        final_vf = f"{color_grade},{sub_filter}"

        final_cmd = [
            "ffmpeg", "-y",
            "-i", str(temp_visual_mp4),
            "-i", str(mixed_audio_path),
            "-vf", final_vf,
            "-c:v", "libx264",
            "-preset", "medium",
            "-crf", "18",
            "-c:a", "aac",
            "-b:a", "192k",
            "-shortest",
            "-pix_fmt", "yuv420p",
            str(final_mp4)
        ]

        logger.info(f"Rendering final MP4 with burning subtitles -> {final_mp4}")
        try:
            res = subprocess.run(final_cmd, capture_output=True, text=True, check=True)
            for seg in scene_segments:
                try: seg.unlink()
                except Exception: pass
            try: concat_txt.unlink()
            except Exception: pass
            try: temp_visual_mp4.unlink()
            except Exception: pass
            return True, final_mp4, "SUCCESS"
        except subprocess.CalledProcessError as e:
            logger.error(f"Final composition failed: {e.stderr}")
            return False, final_mp4, f"Final composition failed: {e.stderr[:200]}"
