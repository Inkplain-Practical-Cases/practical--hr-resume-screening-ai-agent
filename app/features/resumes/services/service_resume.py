"""STEP-2 resume service: extract only explicit job-related keywords from synthetic text."""
from app.features.resumes.providers.qualifications import extract_qualifications

def service_resume(value:str)->str:
    """Report explicit evidence tokens; this is not a hiring recommendation."""
    skills=extract_qualifications(value)
    return "Observed job keywords: "+(", ".join(skills) if skills else "none")
