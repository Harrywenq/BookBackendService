from typing import Optional
from pydantic import BaseModel

class CategoryBase(BaseModel):
    name:str
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    """Schema for create category"""
    pass

class CategoryUpdate(BaseModel):
    """Schema for update category"""
    name: Optional[str] = None
    description: Optional[str] = None

class CategoryInDBBase(CategoryBase):
    id: int

    class Config:
        from_attributes = True #Pydantic read from SQLAlchemy model

class Category(CategoryInDBBase):
    """Schema return for client"""
    pass