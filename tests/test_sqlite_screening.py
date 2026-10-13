"""Ensure SQLite screening metadata has valid links without saving resume content."""
import sqlite3
from app.features.resumes.providers.provider_record_screening import provider_record_screening

def test_screening_run_event_schema(tmp_path):
    file = tmp_path / "screening.sqlite3"
    rid = provider_record_screening("Applicant private CV 1234", "Observed job keywords: python", str(file))
    with sqlite3.connect(file) as con:
        assert con.execute("SELECT status FROM screening_runs WHERE id=?", (rid,)).fetchone()[0] == "completed"
        assert con.execute("SELECT event_type FROM screening_events WHERE screening_id=?", (rid,)).fetchone()[0] == "evidence_extracted"
        assert con.execute("PRAGMA foreign_key_check").fetchall() == []
    assert b"Applicant private CV 1234" not in file.read_bytes()
