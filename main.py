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

import json

def produce_health_short(category: str = None, topic_id: str = None, force_upload: bool = False):
    """
    Executes the complete end-to-end production pipeline:
    1. Topic Discovery & Deduplication (or Content Calendar topic selection)
    2. Hook Generation (3 Variations or approved calendar hook)
    3. Script Writing (Sentence-by-Sentence with 3-step scientific simplification)
    4. Mandatory Female Voice Narration at 1.15x
    5. Sentence-to-Visual Mapping (3D Anatomy + Microscopic + Real Life)
    6. Subtitle Synchronization with Word-Level Highlights
    7. Master Video Composition (1080x1920 30FPS vertical MP4 + Permanent @SwasthSnapYT Watermark)
    8. 18-Point Quality Control Inspection
    9. Thumbnail & Metadata Generation
    10. Staging for YouTube Publication + Clean Shorts Export (Shorts Audio Library Ready)
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
    if topic_id:
        logger.info(f"[STEP 1/10] Loading topic '{topic_id}' from content calendar...")
        cal_entry = db.get_calendar_entry(topic_id)
        if cal_entry:
            sources = cal_entry.get("research_sources")
            if isinstance(sources, str):
                try: sources = json.loads(sources)
                except Exception: sources = [sources]
            topic_data = {
                "topic_id": cal_entry["topic_id"],
                "title": cal_entry["title"],
                "category": cal_entry["category"],
                "core_science": cal_entry["core_concept"],
                "hook": cal_entry["hook_text"],
                "hook_style": "Curiosity Question",
                "term_key": cal_entry.get("term_key"),
                "research_sources": sources or [],
                "visual_style_prompt": cal_entry.get("visual_style_prompt"),
                "bgm_category": cal_entry.get("bgm_category"),
                "status": "planned"
            }
        else:
            topic_data = discovery.discover_topic(preferred_category=category)
            topic_id = topic_data["topic_id"]
    else:
        logger.info("[STEP 1/10] Discovering researched health topic...")
        topic_data = discovery.discover_topic(preferred_category=category)
        topic_id = topic_data["topic_id"]

    logger.info(f"Target Topic: '{topic_data['title']}' [Category: {topic_data['category']}] (ID: {topic_id})")
    db.save_topic(topic_data)
    db.update_calendar_stage(topic_id, research_status="VERIFIED")

    # STEP 2: Generate 3 Hook Variations & Select Strongest
    logger.info("[STEP 2/10] Preparing approved opening hook...")
    if topic_data.get("hook"):
        selected_hook_text = topic_data["hook"]
        hook_data = {
            "hooks": [
                {
                    "style": topic_data.get("hook_style", "Curiosity Question"),
                    "text": selected_hook_text,
                    "highlight_words": ["dimaag", "brain", "acid", "liver", "body", "secret", "truth"],
                    "selected": True
                }
            ],
            "selected_index": 0
        }
    else:
        hook_data = hook_agent.generate_hooks(
            title=topic_data["title"],
            category=topic_data["category"],
            core_science=topic_data["core_science"]
        )
    selected_hook = hook_data["hooks"][hook_data.get("selected_index", 0)]
    logger.info(f"Selected Hook [{selected_hook['style']}]: \"{selected_hook['text']}\"")
    db.update_topic_status(topic_id, status="hook_approved", hook=selected_hook["text"], hook_style=selected_hook["style"])

    # STEP 3: Script Generation
    logger.info("[STEP 3/10] Writing sentence-by-sentence Hinglish script with 3-step scientific simplification...")
    script_data = script_writer.generate_script(topic=topic_data, hook_data=hook_data)
    scenes = script_data.get("scenes", [])
    logger.info(f"Generated {len(scenes)} structured sentence scenes.")
    db.update_calendar_stage(topic_id, script_status="SCRIPT_READY")

    # STEP 4: Mandatory Female Voice Narration (1.15x Speed)
    logger.info(f"[STEP 4/10] Synthesizing female narration at {VOICE_SPEED}x speed using {DEFAULT_VOICE}...")
    voice_ok, raw_voice, mixed_audio, mapped_scenes, word_bounds = voice_manager.synthesize_script(
        topic_id=topic_id,
        scenes=scenes,
        category=topic_data.get("bgm_category") or topic_data["category"]
    )
    if not voice_ok:
        raise RuntimeError("Voice synthesis failed.")
    total_audio_duration = mapped_scenes[-1]["end_sec"]
    logger.info(f"Narration synthesized successfully! Duration: {total_audio_duration:.2f}s")
    db.save_sentence_scenes(topic_id, mapped_scenes)
    db.update_calendar_stage(topic_id, voice_status="VOICE_READY")

    # STEP 5: Sentence-to-Visual Mapping
    logger.info("[STEP 5/10] Mapping each sentence to contextually relevant visuals...")
    enriched_scenes = visual_mapper.map_scenes_to_visuals(
        topic_id=topic_id,
        category=topic_data["category"],
        scenes=mapped_scenes
    )
    db.update_calendar_stage(topic_id, visual_status="ASSETS_READY")

    # STEP 6: Word-Level Subtitles
    logger.info("[STEP 6/10] Generating word-highlighted ASS subtitles...")
    subs_dir = OUTPUT_DIR / "scripts"
    subs_dir.mkdir(parents=True, exist_ok=True)
    ass_path = subs_dir / f"{topic_id}_subtitles.ass"
    sub_generator.generate_ass_subtitles(
        word_boundaries=word_bounds,
        output_ass_path=ass_path
    )

    # STEP 7: Video Composition (1080x1920 30FPS MP4 + @SwasthSnapYT Watermark)
    logger.info("[STEP 7/10] Composing 1080x1920 30FPS vertical MP4 video with permanent @SwasthSnapYT watermark...")
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
    db.update_calendar_stage(topic_id, render_status="RENDERED", video_path=str(video_path))

    # Dual Export: Clean Shorts Version (with Watermark and zero BGM for YouTube Shorts Audio Picker)
    clean_shorts_dir = OUTPUT_DIR / "shorts_audio_ready"
    clean_shorts_dir.mkdir(parents=True, exist_ok=True)
    clean_shorts_mp4 = clean_shorts_dir / f"{topic_id}_clean_shorts.mp4"
    clean_shorts_audio = clean_shorts_dir / f"{topic_id}_clean_narration.mp3"
    voice_manager.audio_mixer.export_clean_shorts_version(
        voiceover_path=raw_voice,
        output_audio_path=clean_shorts_audio,
        video_input_path=video_path,
        output_video_path=clean_shorts_mp4
    )

    # STEP 8: Quality Control (18 Gates)
    logger.info("[STEP 8/10] Running 18 Quality Control gates...")
    qc_passed, qc_results, qc_report_md = qc_agent.inspect_video(
        topic_data={**topic_data, "voice_id": DEFAULT_VOICE, "voice_speed": VOICE_SPEED, "clean_shorts_path": str(clean_shorts_mp4)},
        scenes=enriched_scenes,
        video_path=video_path,
        audio_path=mixed_audio,
        ass_subtitles_path=ass_path
    )
    db.update_topic_status(topic_id, status="qc_passed" if qc_passed else "qc_failed", qc_passed=qc_passed, qc_report=qc_report_md)
    db.update_calendar_stage(topic_id, qc_status="QC_PASSED" if qc_passed else "QC_FAILED", approval_status="APPROVED" if qc_passed else "REJECTED")
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
    logger.info("[STEP 10/10] Staging for YouTube publishing (AUTO_UPLOAD=false, private staging)...")
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
    logger.info(f"Rendered Master Video: {video_path}")
    logger.info(f"Clean Shorts Video: {clean_shorts_mp4}")
    logger.info(f"QC Audit Report: {OUTPUT_DIR / 'reports' / f'{topic_id}_qc_report.md'}")
    logger.info("==================================================")

    return True, topic_id, video_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Health Videos Production Engine")
    parser.add_argument("--run-once", action="store_true", help="Execute single video production cycle")
    parser.add_argument("--topic-id", type=str, default=None, help="Target specific topic ID (e.g. day01_video01)")
    parser.add_argument("--category", type=str, default="Sleep Science", help="Preferred medical category")
    parser.add_argument("--schedule", action="store_true", help="Run 2x daily automated scheduler daemon")
    parser.add_argument("--upload", action="store_true", help="Force private upload to YouTube")

    args = parser.parse_args()

    if args.schedule:
        from scheduler.cron_runner import AutomationScheduler
        scheduler = AutomationScheduler(production_callback=lambda: produce_health_short(category=args.category))
        scheduler.start()
    else:
        produce_health_short(category=args.category, topic_id=args.topic_id, force_upload=args.upload)
