"""HTTP door: validate typed request and delegate to handler.
ICS layer: door
CRD component: be.receive_resume
Called by: REST clients
Calls: handle_resume
Why: keeps HTTP and business rules separate.
Without: validation and orchestration become coupled.
Step: added in STEP-1.
"""
from fastapi import APIRouter
from pydantic import BaseModel, Field
from app.features.resumes.handlers.handle_resume import handle_resume
router = APIRouter(prefix="/api", tags=["resumes"])
class ResumeRequest(BaseModel):
    document_text: str = Field(min_length=3, max_length=2500)
class ResumeResponse(BaseModel):
    status: str
    detail: str
@router.post("/resumes", response_model=ResumeResponse)
def receive_resume(request: ResumeRequest) -> ResumeResponse:
    # Every request is validated before the handler sees it.
    return ResumeResponse(**handle_resume(request.document_text))
