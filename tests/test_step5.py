from app.features.resumes.services.recruiter_review import record_recruiter_review

def test_review_has_human_provenance():
    out=record_recruiter_review({"finding":"unknown"},"reviewer-1","Insufficient evidence")
    assert out["automated_decision"] is None
    assert out["review"]["reviewer_id"]=="reviewer-1"
