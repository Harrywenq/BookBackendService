from typing import Optional
from pydantic import BaseModel

class AuthorBase(BaseModel):
    name:str
    bio: Optional[str] = None

class AuthorCreate(AuthorBase):
    """Schema for create author"""
    pass

class AuthorUpdate(BaseModel):
    """Schema for update author"""
    name: Optional[str] = None
    bio: Optional[str] = None

class AuthorInDBBase(AuthorBase):
    id: int

    class Config:
        from_attributes = True #Pydantic read from SQLAlchemy model

class Author(AuthorInDBBase):
    """Schema return for client"""
    pass