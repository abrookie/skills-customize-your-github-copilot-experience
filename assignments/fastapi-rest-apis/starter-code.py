from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel


app = FastAPI(title="Book API")


class Book(BaseModel):
    id: int
    title: str
    author: str


books = [
    {"id": 1, "title": "The Giver", "author": "Lois Lowry"},
    {"id": 2, "title": "Fahrenheit 451", "author": "Ray Bradbury"},
]


# Task 1: Return every book in the collection.
@app.get("/books")
def get_books():
    pass


# Task 1: Add a new book and return it with status code 201.
@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: Book):
    pass


# Task 2: Return one book or a 404 error when it does not exist.
@app.get("/books/{book_id}")
def get_book(book_id: int):
    pass