import sqlite3

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel


DATABASE_FILE = "books.db"
app = FastAPI(title="Persistent Book API")


class BookInput(BaseModel):
    title: str
    author: str


def get_connection():
    connection = sqlite3.connect(DATABASE_FILE)
    connection.row_factory = sqlite3.Row
    return connection


def create_books_table():
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL
            )
            """,
        )


@app.on_event("startup")
def setup_database():
    # Task 1: Create the database table before requests arrive.
    pass


@app.get("/books")
def get_books():
    # Task 1: Read every book from SQLite and return JSON-friendly dictionaries.
    pass


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: BookInput):
    # Task 1: Insert a book, then return it with its generated ID.
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    with get_connection() as connection:
        row = connection.execute(
            "SELECT id, title, author FROM books WHERE id = ?", (book_id,)
        ).fetchone()

    if row is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return dict(row)


@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookInput):
    # Task 2: Update the matching book or raise a 404 error.
    pass


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    # Task 2: Delete the matching book or raise a 404 error.
    pass