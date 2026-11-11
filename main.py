#!/usr/bin/env python3
"""
MASTER PRODUCTION PIPELINE ORCHESTRATOR
Health Videos: Premium AI Health & Science YouTube Shorts Automation Engine
"""

import sys
import os
from pathlib import Path

# Auto-bootstrap project virtual environment if executed via system Python
ROOT_PATH = Path(__file__).resolve().parent
venv_python = ROOT_PATH / "venv" / "bin" / "python3"
if (sys.prefix == sys.base_prefix) and venv_python.exists():
    os.execv(str(venv_python), [str(venv_python)] + sys.argv)

import argparse
import logging
from datetime import datetime

# Setup root path
sys.path.insert(0, str(ROOT_PATH))

from config.settings import LOGS_DIR, OUTPUT_DIR, DEFAULT_VOICE, VOICE_SPEED
from database.db_manager import DatabaseManager
from research.topic_discovery import TopicDiscoveryEngine
from content.hook_generator import HookGeneratorAgent
from content.script_writer import ScriptWriterEngine
from voice.voice_manager import VoiceManager
from visual.sentence_mapper import SentenceVisualMapper
from visual.subtitle_generator import SubtitleGenerator
from visual.video_composer import VideoComposer
from qc.quality_control import QualityControlAgent
from youtube.metadata_generator import MetadataGenerator
from youtube.thumbnail_generator import ThumbnailGenerator
from youtube.publisher import YouTubePublisher

# Logging configuration
LOGS_DIR.mkdir(parents=True, exist_ok=True)
log_file = LOGS_DIR / f"pipeline_{datetime.now().strftime('%Y%m%d')}.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("health_videos.master")

def produce_health_short(category: str = None, force_upload: bool = False):
    """
    Executes the complete end-to-end production pipeline:
    1. Topic Discovery & Deduplication
    2. Hook Generation (3 Variations)
    3. Script Writing (Sentence-by-Sentence)
    4. Mandatory Female Voice Narration at 1.15x
    5. Sentence-to-Visual Mapping (3D Anatomy + Microscopic + Real Life)
    6. Subtitle Synchronization with Word-Level Highlights
    7. Master Video Composition (1080x1920 30FPS vertical MP4)
    8. 15-Point Quality Control Inspection
    9. Thumbnail & Metadata Generation
    10. Staging for YouTube Publication
    """
    logger.info("==================================================")
    logger.info("STARTING HEALTH VIDEOS PRODUCTION CYCLE")
    logger.info("==================================================")

    db = DatabaseManager()
    discovery = TopicDiscoveryEngine(db=db)
    hook_agent = HookGeneratorAgent()
    script_writer = ScriptWriterEngine()
    voice_manager = VoiceManager()
    visual_mapper = SentenceVisualMapper()
    sub_generator = SubtitleGenerator()
    composer = VideoComposer()
    qc_agent = QualityControlAgent()
    meta_gen = MetadataGenerator()
    thumb_gen = ThumbnailGenerator()
    publisher = YouTubePublisher(db=db)

    # STEP 1: Discover & Research Topic
    logger.info("[STEP 1/10] Discovering researched health topic...")
    topic_data = discovery.discover_topic(preferred_category=category)
    topic_id = topic_data["topic_id"]
    logger.info(f"Discovered Topic: '{topic_data['title']}' [Category: {topic_data['category']}]")
    db.save_topic(topic_data)

    # STEP 2: Generate 3 Hook Variations & Select Strongest
    logger.info("[STEP 2/10] Generating 3 Hook variations...")
    hook_data = hook_agent.generate_hooks(
        title=topic_data["title"],
        category=topic_data["category"],
        core_science=topic_data["core_science"]
    )
    selected_hook = hook_data["hooks"][hook_data.get("selected_index", 0)]
    logger.info(f"Selected Hook [{selected_hook['style']}]: \"{selected_hook['text']}\"")
    db.update_topic_status(topic_id, status="hook_approved", hook=selected_hook["text"], hook_style=selected_hook["style"])

    # STEP 3: Script Generation
    logger.info("[STEP 3/10] Writing sentence-by-sentence Hinglish script...")
    script_data = script_writer.generate_script(topic=topic_data, hook_data=hook_data)
    scenes = script_data.get("scenes", [])
    logger.info(f"Generated {len(scenes)} structured sentence scenes.")

    # STEP 4: Mandatory Female Voice Narration (1.15x Speed)
    logger.info(f"[STEP 4/10] Synthesizing female narration at {VOICE_SPEED}x speed using {DEFAULT_VOICE}...")
    voice_ok, raw_voice, mixed_audio, mapped_scenes, word_bounds = voice_manager.synthesize_script(
        topic_id=topic_id,
        scenes=scenes,
        category=topic_data["category"]
    )
    if not voice_ok:
        raise RuntimeError("Voice synthesis failed.")
    total_audio_duration = mapped_scenes[-1]["end_sec"]
    logger.info(f"Narration synthesized successfully! Duration: {total_audio_duration:.2f}s")
    db.save_sentence_scenes(topic_id, mapped_scenes)

    # STEP 5: Sentence-to-Visual Mapping
    logger.info("[STEP 5/10] Mapping each sentence to contextually relevant visuals...")
    enriched_scenes = visual_mapper.map_scenes_to_visuals(
        topic_id=topic_id,
        category=topic_data["category"],
        scenes=mapped_scenes
    )

    # STEP 6: Word-Level Subtitles
    logger.info("[STEP 6/10] Generating word-highlighted ASS subtitles...")
    subs_dir = OUTPUT_DIR / "scripts"
    subs_dir.mkdir(parents=True, exist_ok=True)
    ass_path = subs_dir / f"{topic_id}_subtitles.ass"
    sub_generator.generate_ass_subtitles(
        word_boundaries=word_bounds,
        output_ass_path=ass_path
    )

    # STEP 7: Video Composition (1080x1920 30FPS MP4)
    logger.info("[STEP 7/10] Composing 1080x1920 30FPS vertical MP4 video...")
    render_ok, video_path, render_msg = composer.compose_short(
        topic_id=topic_id,
        scenes=enriched_scenes,
        mixed_audio_path=mixed_audio,
        ass_subtitles_path=ass_path,
        total_duration=total_audio_duration
    )
    if not render_ok or not video_path.exists():
        raise RuntimeError(f"Video rendering failed: {render_msg}")
    logger.info(f"Video rendered successfully: {video_path} ({video_path.stat().st_size} bytes)")
    db.update_topic_status(topic_id, status="rendered", video_path=str(video_path), duration_actual=total_audio_duration)

    # STEP 8: Quality Control (15 Gates)
    logger.info("[STEP 8/10] Running 15 Quality Control gates...")
    qc_passed, qc_results, qc_report_md = qc_agent.inspect_video(
        topic_data={**topic_data, "voice_id": DEFAULT_VOICE, "voice_speed": VOICE_SPEED},
        scenes=enriched_scenes,
        video_path=video_path,
        audio_path=mixed_audio,
        ass_subtitles_path=ass_path
    )
    db.update_topic_status(topic_id, status="qc_passed" if qc_passed else "qc_failed", qc_passed=qc_passed, qc_report=qc_report_md)
    logger.info(f"Quality Control Result: {'PASSED' if qc_passed else 'FAILED'}")

    # STEP 9: Thumbnail & Metadata Generation
    logger.info("[STEP 9/10] Generating cinematic thumbnail and YouTube SEO metadata...")
    metadata = meta_gen.generate_metadata(
        title=topic_data["title"],
        category=topic_data["category"],
        core_science=topic_data["core_science"],
        sources=topic_data.get("research_sources", [])
    )
    
    # Use first scene visual or reference image for thumbnail
    first_visual = enriched_scenes[0].get("asset_path")
    thumb_bg = Path(first_visual) if first_visual and Path(first_visual).suffix in ('.png', '.jpg', '.jpeg') else (ROOT_PATH / "assets" / "references" / "media_1794379567781.png")
    thumbnail_path = thumb_gen.generate_thumbnail(
        topic_id=topic_id,
        headline=enriched_scenes[0].get("text_overlay", "3D BODY SCIENCE"),
        background_image=thumb_bg
    )
    db.update_topic_status(topic_id, thumbnail_path=str(thumbnail_path))

    # STEP 10: Publishing Preparation & Safe Staging
    logger.info("[STEP 10/10] Staging for YouTube publishing...")
    pub_result = publisher.publish_video(
        topic_id=topic_id,
        video_path=video_path,
        metadata=metadata,
        thumbnail_path=thumbnail_path,
        force_upload=force_upload
    )
    logger.info(f"Publishing Status: {pub_result.get('status')} - {pub_result.get('message', '')}")

    logger.info("==================================================")
    logger.info("PRODUCTION CYCLE COMPLETED SUCCESSFULLY!")
    logger.info(f"Rendered Video: {video_path}")
    logger.info(f"QC Audit Report: {OUTPUT_DIR / 'reports' / f'{topic_id}_qc_report.md'}")
    logger.info("==================================================")

    return True, topic_id, video_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Health Videos Production Engine")
    parser.add_argument("--run-once", action="store_true", help="Execute single video production cycle")
    parser.add_argument("--category", type=str, default="Sleep Science", help="Preferred medical category")
    parser.add_argument("--schedule", action="store_true", help="Run 2x daily automated scheduler daemon")
    parser.add_argument("--upload", action="store_true", help="Force private upload to YouTube")

    args = parser.parse_args()

    if args.schedule:
        from scheduler.cron_runner import AutomationScheduler
        scheduler = AutomationScheduler(production_callback=lambda: produce_health_short(category=args.category))
        scheduler.start()
    else:
        produce_health_short(category=args.category, force_upload=args.upload)
