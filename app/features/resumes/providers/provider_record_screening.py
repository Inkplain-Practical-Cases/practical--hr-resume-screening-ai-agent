"""Persist only privacy-safe resume screening metadata, never applicant personal data."""
import os
import sqlite3
from pathlib import Path
from uuid import uuid4
from datetime import datetime, timezone

def provider_record_screening(document_text: str, result: str, db_path: str | None = None) -> str:
    """Store one completed screening run and its linked audit event, excluding resume text."""
    path = db_path or os.getenv("INKPLAIN_SCREENING_DB", "data/resume_screening.sqlite3")
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    screening_id = uuid4().hex
    at = datetime.now(timezone.utc).isoformat()
    with sqlite3.connect(path) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute("""CREATE TABLE IF NOT EXISTS screening_runs (
            id TEXT PRIMARY KEY,
            document_char_count INTEGER NOT NULL,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL
        )""")
        connection.execute("""CREATE TABLE IF NOT EXISTS screening_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            screening_id TEXT NOT NULL REFERENCES screening_runs(id),
            event_type TEXT NOT NULL,
            result_char_count INTEGER NOT NULL,
            occurred_at TEXT NOT NULL
        )""")
        connection.execute("INSERT INTO screening_runs(id, document_char_count, status, created_at) VALUES (?, ?, ?, ?)",
                           (screening_id, len(document_text), "completed", at))
        connection.execute("INSERT INTO screening_events(screening_id, event_type, result_char_count, occurred_at) VALUES (?, ?, ?, ?)",
                           (screening_id, "evidence_extracted", len(result), at))
    return screening_id
