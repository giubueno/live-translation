from typing import Union, List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Source, Language, Event

app = FastAPI()

# Apply the CORSMiddleware with the most permissive settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,  # Allows cookies to be included in CORS requests
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Mock data

translations = {
    "english": ["Hello"],
    "spanish": ["Hola"],
    "portuguese": ["Olá"],
    "russian": ["Привет"],
    "chinese": ["你好"],
    "arabic": ["مرحبا"],
    "turkish": ["Merhaba"]
}

@app.get("/")
def read_root():
    return {"version": "0.1.0"}

# HEALTH endpoints

@app.get("/ready")
def ready_probe():
    return {"status": "ready"}

@app.get("/live")
def live_probe():
    return {"status": "live"}

@app.get("/translations/{language}")
def read_translation(language: str, q: Union[str, None] = None) -> str:
    if not translations:
        return None

    return translations[language][-1]

@app.post("/translations")
def create_translation(language: dict) -> dict:
    translations.append(translation)
    return translation