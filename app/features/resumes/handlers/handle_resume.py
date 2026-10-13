"""Resume handler coordinates evidence extraction and minimal durable audit."""
from app.features.resumes.services.service_resume import service_resume
from app.features.resumes.services.service_record_screening import service_record_screening

def handle_resume(value: str) -> dict[str, str]:
    """Keep existing API behavior; never store applicant CV text or screening narrative."""
    detail = service_resume(value)
    service_record_screening(value, detail)
    return {"status": "accepted", "detail": detail}
