"""
Python Exception Handling Starter Code
Students should extend this to complete the assignment.
"""

import csv
import logging
from typing import List, Dict

# Configure logging for error tracking
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


# TODO: Define custom exception classes here
# Example: class InvalidAgeError(Exception): pass


def read_csv_file(filename: str) -> List[Dict]:
    """
    Read a CSV file and return data as a list of dictionaries.
    
    Args:
        filename: Path to the CSV file
        
    Returns:
        List of dictionaries containing the CSV data
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        TODO: Document other exceptions this function raises
    """
    # TODO: Implement this function with error handling
    pass


def parse_integer_input(user_input: str) -> int:
    """
    Convert user input string to an integer.
    
    Args:
        user_input: String input from user
        
    Returns:
        Converted integer value
        
    Raises:
        ValueError: If the input cannot be converted to an integer
    """
    # TODO: Implement this function with error handling
    pass


def access_list_element(data_list: list, index: int) -> any:
    """
    Safely access a list element by index.
    
    Args:
        data_list: The list to access
        index: The index to retrieve
        
    Returns:
        The element at the specified index
        
    Raises:
        IndexError: If the index is out of range
        TypeError: If data_list is not a list
    """
    # TODO: Implement this function with error handling
    pass


def validate_user_age(age: int) -> bool:
    """
    Validate that age is within acceptable range.
    
    Args:
        age: The age value to validate
        
    Returns:
        True if age is valid
        
    Raises:
        TODO: Define and raise a custom exception for invalid age
    """
    # TODO: Implement this function with custom exception
    pass


def safe_file_operation(filename: str) -> None:
    """
    Demonstrate safe file operations with try-except-finally.
    
    Args:
        filename: Path to the file to process
    """
    # TODO: Implement this function demonstrating:
    # - try: open and read file
    # - except: handle FileNotFoundError
    # - finally: ensure file is closed
    pass


def operation_with_retry(func, max_retries: int = 3) -> any:
    """
    Execute a function with retry logic.
    
    Args:
        func: Function to execute
        max_retries: Maximum number of retry attempts
        
    Returns:
        Result of successful function execution
        
    Raises:
        Exception: If all retries fail
    """
    # TODO: Implement retry logic with exponential backoff
    pass


if __name__ == "__main__":
    # Example usage - students should test their implementations here
    try:
        # TODO: Test your functions here
        print("Testing exception handling functions...")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
