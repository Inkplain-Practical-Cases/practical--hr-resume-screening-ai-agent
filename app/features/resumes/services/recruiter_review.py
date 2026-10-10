"""Human review state for evidence summaries; avoids automated hiring decisions."""
from datetime import datetime,timezone

def record_recruiter_review(comparison:dict,reviewer_id:str,comment:str)->dict:
    """Attach explicit review provenance; never return a hiring recommendation."""
    if not reviewer_id or not comment.strip():raise ValueError("Review identity and note required")
    return {"comparison":comparison,"review":{"reviewer_id":reviewer_id,"note":comment.strip(),
      "reviewed_at":datetime.now(timezone.utc).isoformat()},"automated_decision":None}
