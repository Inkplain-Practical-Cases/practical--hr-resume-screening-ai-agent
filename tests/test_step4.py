from app.features.resumes.services.evidence_comparison import compare_requirement

def test_unknown_if_no_evidence():
    out=compare_requirement("kubernetes",[{"id":"cv:1","text":"Python developer"}])
    assert out["finding"]=="unknown"
    assert out["human_review_required"]
    assert out["automated_hiring_decision"] is False
