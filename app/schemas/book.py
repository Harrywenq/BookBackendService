from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from app.schemas.author import Author
from app.schemas.category import Category

class BookBase(BaseModel):
    title: str
    description: str
    published_year: int
    category_id: int
    author_id: int

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    published_year: Optional[int] = None
    category_id: Optional[int] = None
    author_id: Optional[int] = None

class BookResponse(BaseModel):
    id: int
    title: str
    description: str
    published_year: int
    category_id: int
    author_id: int
    cover_image: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    author: Author
    category: Category

    class Config:
        orm_mode = True


