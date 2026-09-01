# 📘 Assignment: FastAPI CRUD with SQLite

## 🎯 Objective

Extend a FastAPI application so its book data is stored in a SQLite database instead of an in-memory list. You will implement full CRUD behavior and return useful HTTP responses for successful and missing-book requests.

## 📝 Tasks

### 🛠️ Persist Books with SQLite

#### Description
Complete the collection endpoints in the starter application. Use the provided SQLite connection and table-creation function so new books remain available after the API restarts.

#### Requirements
Completed program should:

- Call `create_books_table()` when the application starts
- Implement `GET /books` to return every book stored in the `books` table
- Implement `POST /books` to insert a JSON book with `title` and `author`
- Return the newly created book, including its database-generated `id`, with HTTP status code `201`
- Run with `uvicorn starter-code:app --reload` and confirm the endpoints work in `/docs`


### 🛠️ Update and Delete Books

#### Description
Add endpoints that modify and remove one book using its ID. Each endpoint must return a `404` response when the requested book does not exist.

#### Requirements
Completed program should:

- Implement `PUT /books/{book_id}` to update a book's title and author
- Implement `DELETE /books/{book_id}` to remove a book and return HTTP status code `204`
- Raise `HTTPException(status_code=404, detail="Book not found")` when an update or deletion affects no book
- Verify an updated book with `GET /books/{book_id}` and verify that a deleted book returns `404`
