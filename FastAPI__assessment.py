from fastapi import FastAPI, HTTPException, BackgroundTasks, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    publication_year: int

class Review(BaseModel):
    text: str
    rating: int

database = {
    "books": [],
    "reviews": [],
}

@app.post("/books/", response_model=Book)
async def add_book(book: Book):
    database["books"].append(book)
    return book

@app.post("/reviews/{book_id}", response_model=Review)
async def add_review(book_id: int, review: Review, background_tasks: BackgroundTasks):
    if book_id < 0 or book_id >= len(database["books"]):
        raise HTTPException(status_code=404, detail="Book not found")

    database["reviews"].append({"book_id": book_id, **review.dict()})
    
    background_tasks.add_task(send_confirmation_email, book_id, review.text)

    return review

@app.get("/books/", response_model=List[Book])
async def get_books(author: str = None, publication_year: int = None):
    books = database["books"]
    if author:
        books = [b for b in books if b.author == author]
    if publication_year:
        books = [b for b in books if b.publication_year == publication_year]
    return books

@app.get("/reviews/{book_id}", response_model=List[Review])
async def get_reviews(book_id: int):
    if book_id < 0 or book_id >= len(database["books"]):
        raise HTTPException(status_code=404, detail="Book not found")
    return [r for r in database["reviews"] if r["book_id"] == book_id]

def send_confirmation_email(book_id: int, review_text: str):
    print(f"Sending confirmation email for review on book {book_id}: {review_text}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


# Theoretical Questions
# 1. Explain how FastAPI handles asynchronous requests and its benefits over synchronous code in Python.
# Ans: FastAPI uses the ASGI standard for handling asynchronous requests. This allows handling multiple requests concurrently, improving overall performance and responsiveness compared to synchronous code.

# 2. Describe how dependency injection works in FastAPI and give an example of its practical use.
# Ans: Dependency injection in FastAPI allows injecting dependencies into route functions. For example, the `BackgroundTasks` parameter in the `add_review` endpoint is an example of dependency injection. Practical use includes injecting database connections, authentication, etc.

# 3. Code walkthrough
# The code has been structured to meet the requirements of the task. It defines FastAPI endpoints for CRUD operations on books and reviews, integrates with a hypothetical database, implements a background task for sending simulated confirmation emails, and includes basic error handling.
