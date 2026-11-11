-- Health Videos Master Database Schema
CREATE TABLE IF NOT EXISTS topics (
    topic_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    category TEXT NOT NULL,
    hook TEXT,
    hook_style TEXT,
    research_summary TEXT,
    research_sources TEXT, -- JSON array of URLs and medical journals
    evidence_status TEXT DEFAULT 'verified', -- 'verified', 'emerging', 'established'
    script_text TEXT,
    duration_estimated REAL,
    duration_actual REAL,
    voice_file_path TEXT,
    video_path TEXT,
    thumbnail_path TEXT,
    status TEXT DEFAULT 'discovered', -- 'discovered', 'scripted', 'voiced', 'rendered', 'qc_passed', 'published', 'rejected'
    qc_passed BOOLEAN DEFAULT 0,
    qc_report TEXT,
    upload_id TEXT,
    publication_date TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS sentence_scenes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic_id TEXT NOT NULL,
    sentence_idx INTEGER NOT NULL,
    sentence_text TEXT NOT NULL,
    start_sec REAL NOT NULL,
    end_sec REAL NOT NULL,
    visual_description TEXT,
    visual_type TEXT, -- '3d_anatomy', 'microscopic', 'relatable_footage', 'infographic'
    camera_movement TEXT,
    animation_notes TEXT,
    overlay_text TEXT,
    asset_path TEXT,
    FOREIGN KEY(topic_id) REFERENCES topics(topic_id)
);

CREATE TABLE IF NOT EXISTS publication_log (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic_id TEXT NOT NULL,
    youtube_video_id TEXT,
    visibility TEXT,
    published_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT,
    response_metadata TEXT,
    FOREIGN KEY(topic_id) REFERENCES topics(topic_id)
);

CREATE INDEX IF NOT EXISTS idx_topics_category ON topics(category);
CREATE INDEX IF NOT EXISTS idx_topics_status ON topics(status);
CREATE INDEX IF NOT EXISTS idx_topics_title ON topics(title);

-- Master Video History & Fingerprints (Strict 100% Originality Engine)
CREATE TABLE IF NOT EXISTS video_history (
    video_id TEXT PRIMARY KEY,
    topic_id TEXT NOT NULL,
    main_topic TEXT NOT NULL,
    subtopic TEXT,
    core_scientific_concept TEXT NOT NULL,
    script_text TEXT NOT NULL,
    hook_text TEXT NOT NULL,
    title TEXT NOT NULL,
    scene_descriptions TEXT, -- JSON array of scene visual descriptions
    visual_asset_ids TEXT,   -- JSON array of asset paths/IDs used
    models_animations TEXT,  -- JSON array of 3D models or animation clips used
    camera_angles_movements TEXT, -- JSON array of camera trajectories
    lighting_style TEXT,
    subtitle_text TEXT,
    bgm_track_id TEXT,
    rendered_path TEXT,
    clean_shorts_path TEXT,
    video_fingerprint TEXT UNIQUE, -- SHA256 of normalized text + visual sequence
    originality_score REAL,
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    publishing_status TEXT DEFAULT 'draft',
    FOREIGN KEY(topic_id) REFERENCES topics(topic_id)
);

-- Background Music Usage History (Anti-Repetition Engine)
CREATE TABLE IF NOT EXISTS bgm_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    track_id TEXT NOT NULL,
    track_category TEXT NOT NULL,
    topic_id TEXT,
    used_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    duration_seconds REAL
);

-- Rejected Generation Attempts (Prevents Repeating Failed/Similar Ideas)
CREATE TABLE IF NOT EXISTS rejected_attempts (
    attempt_id INTEGER PRIMARY KEY AUTOINCREMENT,
    attempt_type TEXT NOT NULL, -- 'topic', 'script', 'hook', 'visual_sequence', 'similarity_gating'
    content_payload TEXT NOT NULL,
    rejection_reason TEXT NOT NULL,
    similarity_score REAL,
    matched_entity_id TEXT,
    attempted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_video_history_topic ON video_history(main_topic);
CREATE INDEX IF NOT EXISTS idx_video_history_fingerprint ON video_history(video_fingerprint);
CREATE INDEX IF NOT EXISTS idx_bgm_history_track ON bgm_history(track_id);
CREATE INDEX IF NOT EXISTS idx_rejected_type ON rejected_attempts(attempt_type);

-- Persistent 15-Day Production Calendar (30 Unique Educational Videos)
CREATE TABLE IF NOT EXISTS content_calendar (
    day_number INTEGER NOT NULL,
    video_number INTEGER NOT NULL,
    topic_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    category TEXT NOT NULL,
    core_concept TEXT NOT NULL,
    hook_text TEXT NOT NULL,
    term_key TEXT NOT NULL,
    scientific_term TEXT NOT NULL,
    term_badge_title TEXT NOT NULL,
    term_badge_sub TEXT NOT NULL,
    research_sources TEXT, -- JSON array of medical citations
    visual_style_prompt TEXT,
    bgm_category TEXT DEFAULT 'medical_documentary',
    research_status TEXT DEFAULT 'VERIFIED',
    script_status TEXT DEFAULT 'PLANNED',
    voice_status TEXT DEFAULT 'PLANNED',
    visual_status TEXT DEFAULT 'PLANNED',
    render_status TEXT DEFAULT 'PLANNED',
    qc_status TEXT DEFAULT 'PLANNED',
    approval_status TEXT DEFAULT 'STAGED',
    video_path TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_calendar_day ON content_calendar(day_number);
CREATE INDEX IF NOT EXISTS idx_calendar_video ON content_calendar(video_number);
CREATE INDEX IF NOT EXISTS idx_calendar_status ON content_calendar(render_status);


