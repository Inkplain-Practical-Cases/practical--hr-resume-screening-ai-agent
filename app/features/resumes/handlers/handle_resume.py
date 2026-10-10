"""Handler: forward validated input to domain service.
ICS layer: handler
CRD component: be.handle_resume
Called by: receive_resume
Calls: service_resume
Why: separates orchestration from HTTP.
Without: impossible to evolve business logic independently.
Step: added in STEP-1.
"""
from app.features.resumes.services.service_resume import service_resume
def handle_resume(value: str) -> dict[str,str]:
    """Coordinate one input value and map a stable response contract."""
    return {"status": "accepted", "detail": service_resume(value)}
