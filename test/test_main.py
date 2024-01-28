from fastapi.testclient import TestClient
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import app

client = TestClient(app)

def test_generate_password():
    response = client.post("/generate-password", json={"length": 12, "include_uppercase": True, "include_digits": True})
    assert response.status_code == 200
    assert "password" in response.json()

def test_invalid_criteria():
    response = client.post("/generate-password", json={"length": 8, "include_uppercase": "invalid", "include_digits": True})
    assert response.status_code == 422
