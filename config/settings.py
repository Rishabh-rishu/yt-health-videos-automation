"""
Configuration & Environment Settings for Health Videos Engine
Enforces 1080x1920 30FPS YouTube Shorts specs, mandatory female voice at 1.15x speed,
and safe publishing gates.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Base paths
ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")

# Video Rendering Specifications
VIDEO_WIDTH = int(os.getenv("VIDEO_WIDTH", "1080"))
VIDEO_HEIGHT = int(os.getenv("VIDEO_HEIGHT", "1920"))
VIDEO_FPS = int(os.getenv("VIDEO_FPS", "30"))
VIDEO_ASPECT_RATIO = "9:16"
MIN_DURATION_SECONDS = float(os.getenv("MIN_DURATION_SECONDS", "30.0"))
MAX_DURATION_SECONDS = float(os.getenv("MAX_DURATION_SECONDS", "50.0"))

# YouTube Safe Zone Margins (in pixels)
SAFE_ZONE_TOP = 200     # Top status bar & channel info
SAFE_ZONE_BOTTOM = 460  # Bottom title, audio button, and like/comment buttons
SAFE_ZONE_LEFT = 60
SAFE_ZONE_RIGHT = 120   # Right-side engagement buttons

# MANDATORY Female Voice Narration Configuration
FEMALE_VOICE_ONLY = True  # Strict enforcement
VOICE_SPEED = float(os.getenv("VOICE_SPEED", "1.15"))  # EXACTLY 1.15x
VOICE_RATE_STR = f"+{int(round((VOICE_SPEED - 1.0) * 100))}%"  # "+15%"
NARRATION_LANGUAGE = os.getenv("NARRATION_LANGUAGE", "hinglish")
VOICE_STYLE = os.getenv("VOICE_STYLE", "cinematic_documentary")

# TTS Provider & Voice IDs
TTS_ENGINE = os.getenv("TTS_ENGINE", "edge-tts")  # 'edge-tts' or 'elevenlabs'
EDGE_TTS_VOICE_HINDI = os.getenv("EDGE_TTS_VOICE_HINDI", "hi-IN-SwaraNeural")
EDGE_TTS_VOICE_HINGLISH = os.getenv("EDGE_TTS_VOICE_HINGLISH", "en-IN-NeerjaExpressiveNeural")
DEFAULT_VOICE = EDGE_TTS_VOICE_HINDI

# ElevenLabs Fallback (Only used if explicitly configured with female voice)
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY", "")
ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "")
ELEVENLABS_MODEL_ID = os.getenv("ELEVENLABS_MODEL_ID", "eleven_multilingual_v2")

# AI Content Generation
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")

# Stock B-roll API
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY", "")

# Audio Design & BGM Levels
ENABLE_BGM = os.getenv("ENABLE_BGM", "true").lower() == "true"
BGM_DUCKING_DB = float(os.getenv("BGM_DUCKING_DB", "-20.0"))  # -20dB under female voice
VOICE_VOLUME = 1.0

# YouTube Publishing Gates
AUTO_UPLOAD = os.getenv("AUTO_UPLOAD", "false").lower() == "true"  # Disabled by default
MANUAL_APPROVAL_REQUIRED = True
DAILY_UPLOAD_LIMIT = int(os.getenv("DAILY_UPLOAD_LIMIT", "2"))
VIDEO_VISIBILITY = os.getenv("VIDEO_VISIBILITY", "private")  # Always private first
YOUTUBE_CATEGORY_ID = "27"  # Education
YOUTUBE_CLIENT_SECRETS_FILE = os.getenv("YOUTUBE_CLIENT_SECRETS_FILE", "client_secrets.json")
YOUTUBE_TOKEN_FILE = os.getenv("YOUTUBE_TOKEN_FILE", "token.pickle")

# Scheduling & Timezone
TIMEZONE = "Asia/Kolkata"
SCHEDULE_MORNING_TIME = "12:00"
SCHEDULE_EVENING_TIME = "18:00"

# Directories
CONFIG_DIR = ROOT_DIR / "config"
DATABASE_DIR = ROOT_DIR / "database"
RESEARCH_DIR = ROOT_DIR / "research"
CONTENT_DIR = ROOT_DIR / "content"
VOICE_DIR = ROOT_DIR / "voice"
VISUAL_DIR = ROOT_DIR / "visual"
REMOTION_DIR = ROOT_DIR / "remotion_engine"
QC_DIR = ROOT_DIR / "qc"
YOUTUBE_DIR = ROOT_DIR / "youtube"
SCHEDULER_DIR = ROOT_DIR / "scheduler"
ASSETS_DIR = ROOT_DIR / "assets"
LOGS_DIR = ROOT_DIR / "logs"
OUTPUT_DIR = ROOT_DIR / "output"

DB_PATH = DATABASE_DIR / "health_videos.db"

# 12 Mandatory Medical Categories
CATEGORIES = [
    "Brain and Psychology",
    "Human Body Secrets",
    "Heart and Blood Circulation",
    "Sleep Science",
    "Food and Nutrition",
    "Fitness and Muscle Science",
    "Gut Health",
    "Skin and Hair Science",
    "Disease Awareness",
    "Hormones and Metabolism",
    "Eyes and Human Senses",
    "Immunity and Microbiology"
]
