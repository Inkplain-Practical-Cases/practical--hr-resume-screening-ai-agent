"""STEP-1 integration checks for the typed API and safe acknowledgement."""
from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)
def test_happy_path():
    response=client.post("/api/resumes",json={"document_text":"Example business input"})
    assert response.status_code==200
    assert response.json()["status"]=="accepted"
def test_empty_input_rejected():
    assert client.post("/api/resumes",json={"document_text":""}).status_code==422
