"""
FastAPI REST API Starter Code
Students should extend this to complete the assignment.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

app = FastAPI(
    title="Book Management API",
    description="A REST API for managing a book collection",
    version="1.0.0"
)

# TODO: Define your Pydantic model for Book here
# Include fields: id, name, author, year
# Add validation for year (1000 to current year)


# In-memory storage for books
books_db = [
    {"id": 1, "name": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"id": 2, "name": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"id": 3, "name": "1984", "author": "George Orwell", "year": 1949},
]

next_id = 4


@app.get("/books", response_model=List[dict])
def get_all_books():
    """Retrieve all books from the collection"""
    # TODO: Implement this endpoint
    pass


@app.get("/books/{book_id}", response_model=dict)
def get_book(book_id: int):
    """Retrieve a single book by ID"""
    # TODO: Implement this endpoint
    # Should return 404 if book not found
    pass


@app.post("/books", response_model=dict, status_code=201)
def create_book(book: dict):
    """Create a new book in the collection"""
    # TODO: Implement this endpoint
    # Use Pydantic model for validation
    # Should return 201 Created status
    pass


@app.put("/books/{book_id}", response_model=dict)
def update_book(book_id: int, book: dict):
    """Update an existing book"""
    # TODO: Implement this endpoint
    # Should return 404 if book not found
    pass


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    """Delete a book from the collection"""
    # TODO: Implement this endpoint
    # Should return 404 if book not found
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
