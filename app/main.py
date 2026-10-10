"""FastAPI composition root: register HTTP door only."""
from fastapi import FastAPI
from app.features.resumes.router import router
app = FastAPI(title="Resume Starter Practical Case")
app.include_router(router)
