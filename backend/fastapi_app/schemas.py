from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class IssueCreate(BaseModel):
    title: str
    description: str
    category_id: int
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    photo_url: Optional[str] = None  # This will be just the path or URL

class IssueResponse(BaseModel):
    id: int
    title: str
    description: str
    category_id: int
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    photo: Optional[str] = None  # <- This must match models.Issue
    status: str
    created_at: datetime

    class Config:
        orm_mode = True


class CategoryResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

# schemas.py
class IssueList(BaseModel):
    id: int
    title: str
    description: str
    category_id: int
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    photo: Optional[str] = None
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
