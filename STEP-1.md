# STEP 1 of 6 — Validated Resume Request

Acknowledge receipt of synthetic resume text without making hiring decisions. This is a real, runnable slice, with a FastAPI door → handler → service dependency path.

## Run

```sh
python -m pip install -r requirements.txt
python -m pytest -q
uvicorn app.main:app --reload
```

## Verify
POST `/api/resumes` with JSON field `document_text`: `Example business input`. Expect 200 and status `accepted`; blank or absent input returns 422.

## Design limitation
This STEP only validates and acknowledges the request. It does not pretend to implement later provider, storage, permission or workflow behavior.
