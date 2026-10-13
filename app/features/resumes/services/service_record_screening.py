"""Record one successful screening result without storing CV or applicant details."""
from app.features.resumes.providers.provider_record_screening import provider_record_screening

def service_record_screening(document_text: str, result: str) -> str:
    """Delegate privacy-safe metadata persistence to the provider."""
    return provider_record_screening(document_text, result)
