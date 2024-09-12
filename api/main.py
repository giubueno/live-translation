from typing import Union, List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import redis
import os
import json

REDIS_HOST = os.environ.get("REDIS_HOST", "redis")

app = FastAPI()

cache = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)
cache.set('version', "0.1.6")

# Apply the CORSMiddleware with the most permissive settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,  # Allows cookies to be included in CORS requests
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

class Message(BaseModel):
    language: str
    text: str

class Translation(BaseModel):
    total: int
    messages: List[str]
    language: str
    languages: List[str]

def get_translations():
    translations = cache.get('translations')
    if translations:
        return json.loads(translations)
    
    translations = {}
    set_translations(translations)

    return translations

def set_translations(translations):
    cache.set('translations', json.dumps(translations))

@app.get("/")
def read_root():
    version = cache.get('version')
    return {"version": version}

@app.get("/languages")
def read_languages() -> List[str]:
    translations = get_translations()
    return list(translations.keys())    

@app.get("/translations/{language}")
def read_translation(language: str, q: Union[str, None] = None) -> Translation:
    translations = get_translations()
    if not translations:
        return Translation(language=language, languages=translations.keys(), total=0, messages=[])

    if language not in translations.keys():
        return Translation(language=language, languages=translations.keys(), total=0, messages=[])

    translation = Translation(
        language=language,
        languages=translations.keys(),
        total=len(translations[language]),
        messages=translations[language])

    return translation

@app.post("/translations")
def create_translation(message: Message) -> Message:
    translations = get_translations()
    if message.language not in translations.keys():
        translations[message.language] = []
    
    # prepend the time to the message with only hh:mm
    message.text = f"{datetime.now().strftime('%H:%M')}: {message.text}"
    translations[message.language].append(message.text)
    set_translations(translations)

    return message

@app.post("/translations/reset")
def reset_translation() -> Translation:
    translations = {}
    set_translations(translations)
    return Translation(language="", languages=[], total=0, messages=[])