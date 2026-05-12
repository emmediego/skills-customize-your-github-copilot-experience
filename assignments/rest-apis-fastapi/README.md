# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build a modern REST API using FastAPI, understanding how to create endpoints, handle HTTP requests, manage data validation, and deploy a functional backend service for client applications.

## 📝 Tasks

### 🛠️ Task 1: Create Basic API Endpoints

#### Description
Build the foundation of your REST API by creating basic GET and POST endpoints. You'll set up a FastAPI application with endpoints to retrieve and create book records.

#### Requirements
Your API should:

- Have a GET endpoint (`/books`) that returns a list of all books
- Have a GET endpoint (`/books/{id}`) that returns a single book by ID
- Have a POST endpoint (`/books`) that creates a new book with name, author, and year
- Return appropriate HTTP status codes (200 for success, 201 for created, 404 for not found)
- Store books in an in-memory list for this task


### 🛠️ Task 2: Add Data Validation with Pydantic

#### Description
Implement data validation using Pydantic models to ensure that incoming requests are well-formed and contain valid data types and values.

#### Requirements
Your API should:

- Define a Pydantic `Book` model with fields: `id` (integer), `name` (string), `author` (string), and `year` (integer)
- Validate that `year` is a positive integer between 1000 and the current year
- Validate that `name` and `author` are non-empty strings
- Return a 422 Unprocessable Entity error with helpful validation messages for invalid data
- Use the model in your POST endpoint to validate incoming book data


### 🛠️ Task 3: Implement DELETE and UPDATE Endpoints

#### Description
Extend your API with UPDATE (PUT) functionality and DELETE operations to create a complete CRUD (Create, Read, Update, Delete) API.

#### Requirements
Your API should:

- Implement a PUT endpoint (`/books/{id}`) to update an existing book's information
- Implement a DELETE endpoint (`/books/{id}`) to remove a book
- Return 404 Not Found when attempting to update or delete a book that doesn't exist
- Update the Pydantic model to support partial updates (optional fields) if needed
- Validate all updated data the same way as creation


### 🛠️ Task 4: Add Error Handling and Documentation (Stretch Goal)

#### Description
Enhance your API with robust error handling and interactive API documentation that allows developers to test endpoints directly from their browser.

#### Requirements
Your API should:

- Include custom error responses with clear error messages and appropriate HTTP status codes
- Provide automatic interactive API documentation (FastAPI's built-in Swagger UI at `/docs`)
- Handle edge cases such as invalid IDs (non-integer values) gracefully
- Include descriptive docstrings for all endpoints that appear in the documentation
- Test the API using the interactive Swagger UI documentation
