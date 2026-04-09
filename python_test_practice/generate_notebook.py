import json
import os

# Dictionary containing the notebook names and their respective questions
notebook_data = {
    "1_Functions.ipynb": [
        "Write a function `calculate_factorial(n)` that returns the factorial of a number.",
        "Write a function `is_prime(n)` that checks if a number is prime.",
        "Write a function `fibonacci_sequence(n)` that returns a list of the first n Fibonacci numbers.",
        "Write a function `euclidean_distance(p1, p2)` that takes two tuples representing 2D points and returns the distance between them.",
        "Write a function `is_palindrome(s)` that ignores spaces and case to check if a string is a palindrome.",
        "Write a function `matrix_transpose(matrix)` that takes a 2D list (matrix) and returns its transpose.",
        "Write a function `element_frequency(lst)` that returns a dictionary containing the frequency of each element in a list.",
        "Write a function `compute_gcd(a, b)` to find the greatest common divisor of two numbers.",
        "Write a function `standard_deviation(data)` that calculates the standard deviation of a list of numbers.",
        "Write a function `unique_elements(lst)` that takes a list and returns a new list with unique elements, preserving the original order."
    ],

    "2_Lambda_Map_Filter.ipynb": [
        "Create a lambda function that takes one argument and adds 15 to it.",
        "Create a lambda function that multiplies two arguments and returns the result.",
        "Use `map()` and a lambda function to square all numbers in a given list.",
        "Use `filter()` to extract only the even numbers from a list of integers.",
        "Use `filter()` to extract all positive numbers from a list containing both positive and negative integers.",
        "Use `map()` to convert a list of strings to uppercase.",
        "Use `filter()` and a lambda function to find all palindromes in a list of words.",
        "Use `map()` to extract the length of each word in a list of strings.",
        "Use `filter()` along with a predefined `is_prime` helper function to extract prime numbers from a list.",
        "Combine `map()` and `filter()`: Given a list of numbers, filter out the odd numbers, and then use map to square the remaining even numbers."
    ],

    "3_Recursion.ipynb": [
        "Write a recursive function to find the sum of the first n natural numbers.",
        "Write a recursive function `power(x, n)` to calculate x raised to the power n.",
        "Write a recursive function to reverse a string.",
        "Write a recursive function to count the number of digits in a positive integer.",
        "Write a recursive function to find the sum of the digits of a number.",
        "Write a recursive function to find the maximum element in a list.",
        "Write a recursive function to check if a given string is a palindrome.",
        "Write a recursive function to convert a decimal number to its binary string representation.",
        "Write a recursive function to calculate the nth term of a geometric progression given the first term 'a' and common ratio 'r'.",
        "Implement binary search recursively on a sorted list."
    ],

    "4_Regular_Expressions.ipynb": [
        "Find all words in a string that end with the suffix 'ing'.",
        "Extract all valid IPv4 addresses from a log file text.",
        "Extract all valid MAC addresses (e.g., 00:1A:2B:3C:4D:5E) from a string.",
        "Write a regex pattern to validate a password (must contain at least 8 characters, one uppercase letter, and one number).",
        "Find and extract all HTML tags (e.g., `<div>`, `</a>`) in a string.",
        "Extract all text enclosed within parentheses in a given string.",
        "Validate a hexadecimal color code (e.g., #FFF or #28A745).",
        "Split a string into a list of words using multiple delimiters (comma, space, and semicolon).",
        "Find all dates formatted exactly as DD-MM-YYYY in a given text block.",
        "Write a regex to check if a string contains entirely alphanumeric characters with no spaces or symbols."
    ],

    "5_OOP.ipynb": [
        "Create a `Student` class with attributes `name` and `roll_no`, and a method `display_details()`.",
        "Create a `Rectangle` class initialized with length and width, featuring methods to calculate `area()` and `perimeter()`.",
        "Create a `BankAccount` class with an initial balance, and methods `deposit()` and `withdraw()` that update and print the balance.",
        "Create a base class `Sensor` (with attributes `id` and `location`) and a derived class `TemperatureSensor` (adding attribute `temp_range`).",
        "Implement a `Vector` class representing a 2D mathematical vector. Overload the `+` operator (`__add__`) to allow adding two vectors together.",
        "Create an `Employee` class that keeps track of the total number of employees using a class variable.",
        "Implement a `Library` class that manages a list of books. Include methods to `add_book()` and `display_books()`.",
        "Create a `Shape` base class with an empty `area()` method. Create derived classes `Circle` and `Square` that override the `area()` method (Polymorphism).",
        "Implement encapsulation by creating a `User` class with a private variable `__password` and methods to set and check the password.",
        "Create a `Matrix` class initialized with a 2D list. Add a method `get_dimensions()` that returns a tuple of (rows, columns)."
    ],

    "6_Stack_Implementation.ipynb": [
        "Define a `Stack` class that initializes an empty list to store stack elements.",
        "Implement the `push(item)` method to add an item to the top of the stack.",
        "Implement the `pop()` method. Ensure it returns an appropriate message or raises an error if the stack is underflowed (empty).",
        "Implement the `peek()` method to return the top element without removing it.",
        "Implement an `is_empty()` method returning a boolean indicating if the stack has no elements.",
        "Implement a `size()` method that returns the current number of elements in the stack.",
        "Using your `Stack` class, write a separate function `reverse_string(text)` that reverses a string using stack operations.",
        "Using your `Stack` class, write a function `is_balanced(expression)` to check if a string of parentheses '()', '{}', '[]' is balanced.",
        "Modify the `Stack` class to include a `get_min()` method that returns the minimum element in the stack in O(1) time.",
        "Write a function `sort_stack(stack)` that sorts the elements in a stack using only one additional auxiliary stack."
    ]
}

def create_jupyter_notebook(filename, questions):
    """Generates a standard Jupyter Notebook JSON structure."""
    cells = []

    for i, q in enumerate(questions, 1):
        # Markdown cell for the question
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": [f"### Q{i}\n", f"**Problem:** {q}"]
        })

        # Empty code cell for the answer
        cells.append({
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": []
        })

    notebook_content = {
        "cells": cells,
        "metadata": {
            "language_info": {
                "name": "python"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(notebook_content, f, indent=2)
    print(f"Created: {filename}")

if __name__ == "__main__":
    print("Generating practice notebooks...")
    for filename, questions in notebook_data.items():
        create_jupyter_notebook(filename, questions)
    print("All notebooks generated successfully!")
