from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.api.deps import get_db
from app import models
from app.schemas.book import BookCreate, BookUpdate, BookResponse

router = APIRouter()

@router.get("/", response_model=List[BookResponse])
def list_books(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    author_id: Optional[int] = Query(None),
    category_id: Optional[int] = Query(None),
    year: Optional[int] = Query(None),
    keyword: Optional[str] = Query(None),
):
    """
    Get list books, include filter:
    
    - Book_id
    - category_id
    - year (published_year)
    - keyword (search in title or desc)
    """
    mb = models.Book
    query = db.query(models.Book)
    if author_id is not None:
        query = query.filter(mb.author_id == author_id)
    if category_id is not None:
        query = query.filter(mb.category_id == category_id)
    if year is not None:
        query = query.filter(mb.published_year == year)
    if keyword is not None:
        like_pattern = f"%{keyword}%"
        query = query.filter(
            or_(
                mb.title.ilike(like_pattern),
                mb.description.ilike(like_pattern),
            )
        )
    books = query.offset(skip).limit(limit).all()
    return books

@router.get("/{book_id}", response_model=BookResponse)
def get_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    """
    Get book detail according id
    """
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )
    
    return book

@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(
    book_in: BookCreate,
    db: Session = Depends(get_db)
):
    author = db.query(models.Author).filter(models.Author.id == book_in.author_id).first()

    if not author:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Author does not exists",
        )
    
    category = db.query(models.Category).filter(models.Category.id == book_in.category_id).first()

    if not category:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Category does not exists",
        )
    
    book = models.Book(
        title = book_in.title,
        description = book_in.description,
        published_year = book_in.published_year,
        author_id = book_in.author_id,
        category_id = book_in.category_id,
        )
    db.add(book)
    db.commit()
    db.refresh(book)

    return book

@router.put("/{book_id}", response_model=BookResponse)
def update_book(
    book_id: int,
    book_up: BookUpdate,
    db: Session = Depends(get_db)
):
    """
    Update book
    - Allow update author_id/category_id, but must check exist
    """
    book = db.query(models.Book).filter(models.Book.id == book_id).first()

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )
    
    if book_up.title is not None:
        book.title = book_up.title
    if book_up.description is not None:
        book.description = book_up.description
    if book_up.title is not None:
        book.title = book_up.title
    if book_up.published_year is not None:
        book.published_year = book_up.published_year

    #if update author_id
    if book_up.author_id is not None and book_up.author_id != book.author_id:
        author = db.query(models.Author).filter(models.Author.id == book_up.author_id).first()

    if not author:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="New author does not exists",
        )
    book.author_id = book_up.author_id

    #if update category_id
    if book_up.category_id is not None and book_up.category_id != book.category_id:
        category = db.query(models.Category).filter(models.Category.id == book_up.category_id).first()

    if not category:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="New category does not exists",
        )
    book.category_id = book_up.category_id
    
    db.commit()
    db.refresh(book)

    return book

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete book
    """
    book = db.query(models.Book).filter(models.Book.id == book_id).first()

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )
    
    db.delete(book)
    db.commit()