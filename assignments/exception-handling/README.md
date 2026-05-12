# 📘 Assignment: Python Exception Handling & Error Recovery

## 🎯 Objective

Learn to write robust Python programs that gracefully handle errors instead of crashing. You'll master try-except blocks, understand different exception types, create custom exceptions, and implement defensive programming patterns that make your code reliable in real-world scenarios.

## 📝 Tasks

### 🛠️ Task 1: Catch and Handle Basic Exceptions

#### Description
Build a program that reads a CSV file and validates user input, catching the most common exceptions: `FileNotFoundError`, `ValueError`, and `IndexError`. Your program should continue running even when errors occur.

#### Requirements
Your program should:

- Open and read a CSV file with error handling for when the file doesn't exist
- Parse and convert data types (e.g., string to integer) with `ValueError` handling
- Access list/dictionary elements with `IndexError` handling
- Display user-friendly error messages instead of showing raw Python tracebacks
- Allow the user to retry operations after an error occurs


### 🛠️ Task 2: Handle Multiple Exception Types and Use Finally

#### Description
Expand your error handling to differentiate between different types of errors and ensure cleanup code runs regardless of whether an error occurred.

#### Requirements
Your program should:

- Catch at least three different exception types with specific handlers for each
- Use the generic `Exception` handler as a fallback for unexpected errors
- Include a `finally` block that performs cleanup (e.g., closing files)
- Provide specific, context-aware error messages for each exception type
- Log error information for debugging purposes


### 🛠️ Task 3: Create and Raise Custom Exceptions

#### Description
Implement custom exception classes to handle domain-specific errors that don't fit standard Python exceptions. This makes your code clearer and more maintainable.

#### Requirements
Your program should:

- Define at least two custom exception classes (inherit from `Exception`)
- Raise custom exceptions when business logic constraints are violated (e.g., `InvalidAgeError`, `InsufficientFundsError`)
- Catch custom exceptions with appropriate handling logic
- Include meaningful error messages when raising custom exceptions
- Demonstrate exception inheritance in your custom exception hierarchy


### 🛠️ Task 4: Implement Defensive Programming (Stretch Goal)

#### Description
Apply advanced error handling patterns including exception context (exception chaining), validation, and recovery strategies to make your program production-ready.

#### Requirements
Your program should:

- Use `raise ... from` to chain exceptions and preserve the original error context
- Implement input validation before operations to prevent errors
- Include retry logic with exponential backoff for operations that might temporarily fail
- Use context managers (`with` statements) for safe resource management
- Document which exceptions each function can raise in its docstring
