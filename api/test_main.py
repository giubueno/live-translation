import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# TRANSLATIONS endpoints

def test_read_translations():
    response = client.get("/translations")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_translation():
    translation = {"1": "Hello"}
    response = client.post("/translations", json=translation)
    assert response.status_code == 200
    assert response.json() == translation
