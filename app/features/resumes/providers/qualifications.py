"""Deterministic job keyword extraction, never infer protected attributes."""
import re
SKILLS=("python","fastapi","postgresql","docker","kubernetes","rag","mcp")

def extract_qualifications(text:str)->list[str]:
    """Return tokens explicitly present, not claimed competence levels."""
    words=set(re.findall(r"[a-z]+",text.lower()))
    return [skill for skill in SKILLS if skill in words]
