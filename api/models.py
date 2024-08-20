from pydantic import BaseModel
from datetime import datetime

class Event(BaseModel):
    id: int
    title: str
    description: str
    date: str
    location: str
    image: str
    link: str
    category: str
    tags: str
    isFeatured: bool
    isPublished: bool
    isDeleted: bool
    createdAt: str
    updatedAt: str
    deletedAt: str
    createdBy: int
    updatedBy: int
    deletedBy: int

class Source(BaseModel):
    id: int
    name: str
    url: str
    startsAt: datetime

class Language(BaseModel):
    id: int
    name: str
    code: str
    nativeName: str
    rtl: bool
