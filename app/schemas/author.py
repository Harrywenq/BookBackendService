from typing import Optional
from pydantic import BaseModel

class AuthorBase(BaseModel):
    id: int
    name: str
    bio: Optional[str] = None

    class Config:
        orm_mode = True

class AuthorCreate(BaseModel):
    name: str
    bio: Optional[str] = None

class AuthorUpdate(BaseModel):
    name: Optional[str] = None
    bio: Optional[str] = None

class Author(AuthorBase):
    """Schema return for client"""
    pass