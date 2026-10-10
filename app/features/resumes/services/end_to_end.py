"""Grounded candidate-evidence review pipeline using synthetic input only."""
from app.features.resumes.providers.evidence_index import index_evidence
from app.features.resumes.services.evidence_comparison import compare_requirement
from app.features.resumes.services.recruiter_review import record_recruiter_review

def prepare_recruiter_review(document_id:str,text:str,criteria:list[str],reviewer_id:str)->dict:
    """Create cited claims and request human checking, with no hiring decision."""
    if not reviewer_id:raise PermissionError("Reviewer required")
    passages=index_evidence(document_id,text)
    results=[compare_requirement(criterion,passages) for criterion in criteria]
    return record_recruiter_review({"criteria":results},reviewer_id,"Needs recruiter verification")
