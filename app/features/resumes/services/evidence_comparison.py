"""Job-criterion comparison produces review-only cited evidence, never decisions."""
from app.features.resumes.providers.evidence_index import retrieve_evidence

def compare_requirement(criterion:str,passages:list[dict[str,str]])->dict:
    """Link claim to exact resume evidence, leaving missing evidence unknown."""
    found=retrieve_evidence(passages,criterion)
    return {"criterion":criterion,"evidence":[{"citation":p["id"],"text":p["text"]} for p in found],
            "finding":"evidence_found" if found else "unknown","human_review_required":True,
            "automated_hiring_decision":False}
