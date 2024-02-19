# BSS

#FAST API  documentation

FastAPI Book Review API
This FastAPI-based API allows you to manage books and reviews, including functionalities to add books, submit reviews, retrieve books with filters, and get reviews for a specific book.

Table of Contents
Setup
Usage
API Endpoints
Theoretical Questions

Clone the repository:
git clone https://github.com/your-username/fastapi-book-review-api.git
cd fastapi-book-review-api

Create a virtual environment:
python -m venv venv

Activate the virtual environment:
On Windows:
.\venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Run the FastAPI application:
uvicorn main:app --reload

The API will be accessible at http://127.0.0.1:8000.

Usage
The API provides the following endpoints:

Add a new book:
POST /books/

Submit a review for a book:
POST /reviews/{book_id}

Retrieve all books with filters:
GET /books/

Retrieve all reviews for a specific book:
GET /reviews/{book_id}

Theoretical Questions
Question 1
Explain how FastAPI handles asynchronous requests and its benefits over synchronous code in Python.

Answer:

FastAPI uses the ASGI (Asynchronous Server Gateway Interface) standard to handle asynchronous requests. ASGI allows handling multiple requests concurrently, improving overall performance and responsiveness compared to synchronous code. With asynchronous programming, the server can efficiently manage and process a large number of simultaneous connections without blocking the execution of other tasks. This is particularly beneficial for I/O-bound operations, such as database queries or network requests, where the server can continue processing other requests while waiting for these operations to complete.

Question 2
Describe how dependency injection works in FastAPI and give an example of its practical use.

Answer:

Dependency injection in FastAPI allows injecting dependencies into route functions. For example, the BackgroundTasks parameter in the add_review endpoint is an example of dependency injection. Practical use includes injecting database connections, authentication services, or other resources that a route function may need to execute its logic. By using dependency injection, FastAPI can manage the lifecycle of dependencies, making it easier to test and maintain the code. It also promotes modularity and separation of concerns by allowing dependencies to be defined and managed separately from the route functions.

Question 3
Code walkthrough

The code has been structured to meet the requirements of the task. It defines FastAPI endpoints for CRUD operations on books and reviews, integrates with a hypothetical database, implements a background task for sending simulated confirmation emails, and includes basic error handling.



