#!/usr/bin/env python3
"""
State Synchronization & Durable Persistence Engine for Health Videos
Ensures SQLite database state (content calendar, topics, video history, upload records)
is durably persisted across ephemeral GitHub Actions runners without data loss.

Dual Storage Mechanism:
1. Canonical SQL dump: database/state_dump.sql
2. Structured JSON Ledger: data/production_state.json
"""

import sys
import os
import json
import sqlite3
import logging
from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_PATH))

from config.settings import ROOT_DIR, DB_PATH

logger = logging.getLogger("health_videos.state_sync")

DATA_DIR = ROOT_DIR / "data"
STATE_JSON_PATH = DATA_DIR / "production_state.json"
STATE_SQL_PATH = ROOT_DIR / "database" / "state_dump.sql"
SCHEMA_SQL_PATH = ROOT_DIR / "database" / "schema.sql"

TABLES_TO_PERSIST = [
    "topics",
    "content_calendar",
    "video_history",
    "sentence_scenes",
    "publication_log",
    "bgm_history",
    "rejected_attempts"
]

def export_state(db_file: Path = DB_PATH, json_file: Path = STATE_JSON_PATH, sql_file: Path = STATE_SQL_PATH):
    """Exports SQLite tables into version-controlled JSON and SQL dump."""
    if not db_file.exists():
        logger.warning(f"Database {db_file} not found. Cannot export state.")
        return False

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    sql_file.parent.mkdir(parents=True, exist_ok=True)

    state_data = {
        "version": 1,
        "exported_at": str(sqlite3.datetime.datetime.now()),
        "tables": {}
    }

    conn = sqlite3.connect(str(db_file))
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    for table in TABLES_TO_PERSIST:
        try:
            cursor.execute(f"SELECT * FROM {table}")
            rows = [dict(r) for r in cursor.fetchall()]
            state_data["tables"][table] = rows
        except sqlite3.OperationalError:
            state_data["tables"][table] = []

    # Write JSON
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(state_data, f, indent=2, ensure_ascii=False)

    # Write SQL dump
    with open(sql_file, "w", encoding="utf-8") as f:
        for line in conn.iterdump():
            f.write(f"{line}\n")

    conn.close()
    logger.info(f"Database state successfully exported to {json_file} and {sql_file}")
    return True

def restore_state(db_file: Path = DB_PATH, json_file: Path = STATE_JSON_PATH, sql_file: Path = STATE_SQL_PATH, force: bool = False):
    """Restores SQLite database from JSON or SQL dump on fresh/ephemeral runners."""
    db_file.parent.mkdir(parents=True, exist_ok=True)

    # If DB already has data, check if restoration is needed
    if not force and db_file.exists():
        try:
            conn = sqlite3.connect(str(db_file))
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM content_calendar")
            cal_count = cursor.fetchone()[0]
            conn.close()
            if cal_count > 0:
                logger.info(f"Database {db_file} already exists with {cal_count} calendar entries. No initial restore needed.")
                return True
        except Exception:
            pass

    # Ensure schema is applied first
    if SCHEMA_SQL_PATH.exists():
        conn = sqlite3.connect(str(db_file))
        with open(SCHEMA_SQL_PATH, "r", encoding="utf-8") as f:
            conn.executescript(f.read())
        conn.commit()
        conn.close()

    # Priority 1: Restore from JSON ledger
    if json_file.exists():
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                state_data = json.load(f)

            conn = sqlite3.connect(str(db_file))
            cursor = conn.cursor()

            for table, rows in state_data.get("tables", {}).items():
                if not rows:
                    continue
                # Get columns from first row
                cols = list(rows[0].keys())
                placeholders = ", ".join(["?"] * len(cols))
                col_names = ", ".join(cols)
                stmt = f"INSERT OR REPLACE INTO {table} ({col_names}) VALUES ({placeholders})"

                for r in rows:
                    cursor.execute(stmt, [r[col] for col in cols])

            conn.commit()
            conn.close()
            logger.info(f"Database successfully restored from JSON ledger {json_file}")
            return True
        except Exception as e:
            logger.error(f"Failed to restore from JSON ledger: {e}")

    # Priority 2: Restore from SQL dump
    if sql_file.exists():
        try:
            conn = sqlite3.connect(str(db_file))
            with open(sql_file, "r", encoding="utf-8") as f:
                conn.executescript(f.read())
            conn.commit()
            conn.close()
            logger.info(f"Database successfully restored from SQL dump {sql_file}")
            return True
        except Exception as e:
            logger.error(f"Failed to restore from SQL dump: {e}")

    # Fallback: Seed calendar if empty
    from research.content_bank_30 import seed_calendar_and_topics
    from database.db_manager import DatabaseManager
    seed_calendar_and_topics(DatabaseManager(db_file))
    export_state(db_file, json_file, sql_file)
    logger.info("Initialized fresh database and seeded 15-day calendar.")
    return True

def print_status(db_file: Path = DB_PATH):
    if not db_file.exists():
        print(f"Database {db_file} does not exist.")
        return
    conn = sqlite3.connect(str(db_file))
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    print("\n" + "=" * 60)
    print("  DATABASE PERSISTENCE STATUS AUDIT")
    print("=" * 60)
    for t in TABLES_TO_PERSIST:
        try:
            cur.execute(f"SELECT COUNT(*) FROM {t}")
            cnt = cur.fetchone()[0]
            print(f"  {t:<20}: {cnt} records")
        except Exception as e:
            print(f"  {t:<20}: {e}")
    try:
        cur.execute("SELECT topic_id, title, day_number, video_number FROM content_calendar WHERE approval_status != 'UPLOADED' ORDER BY video_number ASC LIMIT 1")
        nxt = cur.fetchone()
        if nxt:
            print(f"\n  Next Pending Short   : Day {nxt['day_number']} Video #{nxt['video_number']} - {nxt['title']} ({nxt['topic_id']})")
        else:
            print("\n  Next Pending Short   : All 30 topics completed!")
    except Exception:
        pass
    print("=" * 60 + "\n")
    conn.close()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="State sync utility")
    parser.add_argument("--export", action="store_true", help="Export DB to JSON and SQL")
    parser.add_argument("--restore", action="store_true", help="Restore DB from JSON or SQL")
    parser.add_argument("--force-restore", action="store_true", help="Force overwrite DB from JSON/SQL")
    parser.add_argument("--status", action="store_true", help="Print database record counts and next topic")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

    if args.force_restore:
        restore_state(force=True)
    elif args.restore:
        restore_state()
    elif args.status:
        print_status()
    else:
        export_state()
