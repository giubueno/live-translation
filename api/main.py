from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/probes/ready")
def ready_probe():
    return {"status": "ready"}

@app.get("/probes/live")
def live_probe():
    return {"status": "live"}

@app.get("/sources/{source_id}")
def read_source(source_id: int, q: Union[str, None] = None):
    return {"source_id": source_id, "q": q}

@app.get("/languages/{language_id}")
def read_language(language_id: int, q: Union[str, None] = None):
    return {"language_id": language_id, "q": q}

@app.get("/events/{event_id}")
def read_event(event_id: int, q: Union[str, None] = None):
    return {"event_id": event_id, "q": q}