from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.endpoints import authors, books, categories

app = FastAPI(
    title="Book Management API",
    description="Simple API to manage books, authors, categories and book covers",
    version="1.0.0"
)

#Include routes
app.include_router(authors.router, prefix="/authors", tags=["Authors"])
app.include_router(books.router, prefix="/books", tags=["Books"])
app.include_router(categories.router, prefix="/categories", tags=["Categories"])

#Static files covers image

@app.get("/") #127.0.0.1:8000/
def read_root():
    return {"message": "Book management API is running"}