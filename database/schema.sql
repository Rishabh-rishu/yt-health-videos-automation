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
