from typing import Union, List
from fastapi import FastAPI, HTTPException
from models import Source, Language, Event

app = FastAPI()

# Mock data

idioms = {
    1: Language(id=1, name="English", code="en", nativeName="English", rtl=False),
    2: Language(id=2, name="Spanish", code="es", nativeName="Español", rtl=False),
    3: Language(id=3, name="Portuguese", code="pt", nativeName="Português", rtl=False),
    4: Language(id=4, name="Russian", code="ru", nativeName="Русский", rtl=False),
    5: Language(id=5, name="Chinese", code="zh", nativeName="中文", rtl=False),
    6: Language(id=6, name="Arabic", code="ar", nativeName="العربية", rtl=True),
    7: Language(id=7, name="Turkish", code="tr", nativeName="Türkçe", rtl=False)
}

sources = {}

events = {}

@app.get("/")
def read_root():
    return {"version": "0.1.0"}

@app.get("/ready")
def ready_probe():
    return {"status": "ready"}

@app.get("/live")
def live_probe():
    return {"status": "live"}

# SOURCES endpoints
@app.get("/sources")
def read_sources(q: Union[str, None] = None) -> List[Source]:
    return sources.values()

@app.get("/sources/{source_id}")
def read_source(source_id: int, q: Union[str, None] = None) -> Source:
    if source_id not in sources:
        raise HTTPException(status_code=404, detail=f"Source with id {source_id} not found")
    else:
        return sources[source_id]

@app.post("/sources")
def create_source(source: Source) -> Source:
    if source.id in sources:
        raise HTTPException(status_code=400, detail=f"Source with id {source.id} already exists")
    else:
        sources[source.id] = source
        return source

@app.put("/sources/{source_id}")
def update_source(source_id: int, source: Source) -> Source:
    if source_id not in sources:
        raise HTTPException(status_code=404, detail=f"Source with id {source_id} not found")
    else:
        sources[source_id] = source
        return source

@app.delete("/sources/{source_id}")
def delete_source(source_id: int) -> Source:
    if source_id not in sources:
        raise HTTPException(status_code=404, detail=f"Source with id {source_id} not found")
    else:
        source = sources[source_id]
        del sources[source_id]
        return source

# LANGUAGES endpoints

@app.get("/languages")
def read_languages(q: Union[str, None] = None) -> List[Language]:
    return idioms.values()

@app.get("/languages/{language_id}")
def read_language(language_id: int, q: Union[str, None] = None) -> Language:
    if language_id not in idioms:
        raise HTTPException(status_code=404, detail=f"Language with id {language_id} not found")
    else:
        return idioms[language_id]

@app.post("/languages")
def create_language(language: Language) -> Language:
    if language.id in idioms:
        raise HTTPException(status_code=400, detail=f"Language with id {language.id} already exists")
    else:
        idioms[language.id] = language
        return language

@app.put("/languages/{language_id}")
def update_language(language_id: int, language: Language) -> Language:
    if language_id not in idioms:
        raise HTTPException(status_code=404, detail=f"Language with id {language_id} not found")
    else:
        idioms[language_id] = language
        return language

@app.delete("/languages/{language_id}")
def delete_language(language_id: int) -> Language:
    if language_id not in idioms:
        raise HTTPException(status_code=404, detail=f"Language with id {language_id} not found")
    else:
        language = idioms[language_id]
        del idioms[language_id]
        return language

# EVENTS endpoints
@app.get("/events")
def read_events(q: Union[str, None] = None) -> List[Event]:
    return events.values()

@app.get("/events/{event_id}")
def read_event(event_id: int, q: Union[str, None] = None) -> Event:
    if event_id not in events:
        raise HTTPException(status_code=404, detail=f"Event with id {event_id} not found")
    else:
        return events[event_id]

@app.post("/events")
def create_event(event: Event) -> Event:
    if event.id in events:
        raise HTTPException(status_code=400, detail=f"Event with id {event.id} already exists")
    else:
        events[event.id] = event
        return event

@app.put("/events/{event_id}")
def update_event(event_id: int, event: Event) -> Event:
    if event_id not in events:
        raise HTTPException(status_code=404, detail=f"Event with id {event_id} not found")
    else:
        events[event_id] = event
        return event

@app.delete("/events/{event_id}")
def delete_event(event_id: int) -> Event:
    if event_id not in events:
        raise HTTPException(status_code=404, detail=f"Event with id {event_id} not found")
    else:
        event = events[event_id]
        del events[event_id]
        return event
