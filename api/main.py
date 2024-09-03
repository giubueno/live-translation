from typing import Union, List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime

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
}

class Message(BaseModel):
    language: str
    text: str

class Translation(BaseModel):
    total: int
    messages: List[str]
    language: str
    languages: List[str]

@app.get("/")
def read_root():
    return {"version": "0.1.2"}

# HEALTH endpoints

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/languages")
def read_languages() -> List[str]:
    return list(translations.keys())    

@app.get("/translations/{language}")
def read_translation(language: str, q: Union[str, None] = None) -> Translation | None:
    if not translations:
        return None

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
    if message.language not in translations.keys():
        translations[message.language] = []
    
    # prepend the time to the message with only hh:mm
    message.text = f"{datetime.now().strftime('%H:%M')}: {message.text}"
    translations[message.language].append(message.text)
    return message