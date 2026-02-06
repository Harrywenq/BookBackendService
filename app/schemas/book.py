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
    """Schema for create book"""
    pass

class BookUpdate(BaseModel):
    """Schema for update book"""
    title: Optional[str] = None
    description: Optional[str] = None
    published_year: Optional[int] = None
    category_id: Optional[int] = None
    author_id: Optional[int] = None

class BookInDBBase(BookBase):
    id: int
    title: str
    description: str
    published_year: int
    category_id: int
    author_id: int
    cover_image: Optional[str] = None
    created_at: datetime
    update_at: datetime

    class Config:
        from_attributes = True #Pydantic read from SQLAlchemy model

#Schema nested for author and category

class Book(BookInDBBase):
    """Schema return for client"""
    author: Author
    category: Category