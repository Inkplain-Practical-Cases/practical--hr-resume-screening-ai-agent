from app.features.resumes.providers.evidence_index import index_evidence,retrieve_evidence

def test_traceable_passage():
    rows=index_evidence("cv-1","Python engineer\nCustomer support experience")
    assert retrieve_evidence(rows,"python")[0]["id"]=="cv-1:0"
def test_no_unrelated_evidence():
    assert retrieve_evidence(index_evidence("cv-2","Experience in design"),"kubernetes")==[]
