# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI and use HTTP methods, path parameters, and JSON responses to manage a collection of books. By the end, you will be able to run an API locally and test its endpoints in FastAPI's interactive documentation.

## 📝 Tasks

### 🛠️ Create Book Collection Endpoints

#### Description
Complete the starter application so clients can view every book and add a new book to the in-memory collection.

#### Requirements
Completed program should:

- Create a `FastAPI` application named `app`
- Implement `GET /books` to return the complete `books` list as JSON
- Implement `POST /books` to accept a JSON book with `id`, `title`, and `author`
- Add the submitted book to the list and return it with HTTP status code `201`
- Run with `uvicorn starter-code:app --reload` and verify both endpoints at `/docs`


### 🛠️ Find a Book by ID

#### Description
Add an endpoint that uses a path parameter to return one matching book. Respond with a useful HTTP error when the requested ID is not in the collection.

#### Requirements
Completed program should:

- Implement `GET /books/{book_id}` with an integer `book_id` path parameter
- Return the matching book as JSON when its `id` matches `book_id`
- Raise `HTTPException(status_code=404, detail="Book not found")` when no book matches
- Test one successful request and one missing-book request in `/docs`
