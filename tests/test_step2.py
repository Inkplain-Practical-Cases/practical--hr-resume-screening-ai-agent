from app.features.resumes.providers.qualifications import extract_qualifications

def test_explicit_evidence_only():
    assert extract_qualifications("Used Python and FastAPI") == ["python","fastapi"]
def test_no_inferred_attributes():
    assert extract_qualifications("Candidate enjoys basketball") == []
