from app.features.resumes.services.end_to_end import prepare_recruiter_review

def test_end_to_end_cited_evidence():
    r=prepare_recruiter_review("cv-synthetic","Experienced with Python","Python","reviewer") if False else prepare_recruiter_review("cv-synthetic","Experienced with Python",["Python"],"reviewer")
    assert r["comparison"]["criteria"][0]["evidence"][0]["citation"]=="cv-synthetic:0"
    assert r["automated_decision"] is None
