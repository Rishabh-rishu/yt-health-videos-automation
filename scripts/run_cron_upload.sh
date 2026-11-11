#!/usr/bin/env bash
# ==============================================================================
# Swasth Snap (@SwasthSnapYT) — Automated Daily Cron Runner
# Executes 2x daily production and upload (09:30 AM IST and 18:00 PM IST)
# ==============================================================================

set -euo pipefail

PROJECT_DIR="/home/rishabh/Heath Videos"
cd "$PROJECT_DIR"

# Source environment
if [ -f "$PROJECT_DIR/venv/bin/activate" ]; then
    source "$PROJECT_DIR/venv/bin/activate"
fi

# Ensure output and log directories exist
mkdir -p "$PROJECT_DIR/logs" "$PROJECT_DIR/output"

TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S %Z')
echo "=================================================================" >> "$PROJECT_DIR/logs/cron_production.log"
echo "[$TIMESTAMP] Starting scheduled Health Videos production run..." >> "$PROJECT_DIR/logs/cron_production.log"

# Run Python cron runner
"$PROJECT_DIR/venv/bin/python3" "$PROJECT_DIR/scheduler/cron_job_runner.py" >> "$PROJECT_DIR/logs/cron_production.log" 2>&1

EXIT_CODE=$?
echo "[$TIMESTAMP] Cron run finished with exit code: $EXIT_CODE" >> "$PROJECT_DIR/logs/cron_production.log"
echo "=================================================================" >> "$PROJECT_DIR/logs/cron_production.log"

exit $EXIT_CODE
