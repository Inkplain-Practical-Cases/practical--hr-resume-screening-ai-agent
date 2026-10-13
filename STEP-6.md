# STEP 6 of 6 — Integrate and harden resumes

Install dependencies, run `python -m pytest -q`, and start `uvicorn app.main:app`. The full cumulative implementation provides tested local domain behavior and deterministic fixtures. The teaching code does **not** imply production approval, live services or all external adapters are complete. Audit the README limitations before deployment.

## Database (Entity) Relations
STEP-6 adds SQLite `screening_runs` and `screening_events` connected through `screening_id`. Only counts, status and timestamps are saved; neither applicant CV text nor derived evidence text is stored. The database path is `INKPLAIN_SCREENING_DB`. See STEP-6-ERD.
