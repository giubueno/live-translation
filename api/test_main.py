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

# EVENTS endpoints

def test_create_event():
    event = {
        "id": 11,
        "title": "Event 11",
        "description": "",
        "date": "2021-10-10",
        "location": "Berlin",
        "image": "https://placehold.co/600x400",
        "link": "https://example.com",
        "category": "church"
    }
    response = client.post("/events", json=event)
    assert response.status_code == 200
    assert response.json() == event
