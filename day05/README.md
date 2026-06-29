# Day 05 — Python Functions

## What I learned

Today I learned how to use functions in Python.

Main topics:

- how to create a function with `def`
- how to use parameters and arguments
- difference between `print` and `return`
- how to return values from functions
- how to use functions for calculator operations
- how to handle division by zero
- how to validate user input with `while`
- how to handle invalid numbers with `try/except`

## Project: Simple Calculator

The program supports four operations:

1. Addition
2. Subtraction
3. Multiplication
4. Division

The calculator asks the user to choose an operation and enter two numbers.

If the user enters an invalid operation, the program asks again.

If the user enters an invalid number, the program shows an error and asks again.

Division by zero is handled safely.

## Key concepts

### Function

A function is a reusable block of code.

```python
def add(a, b):
    return a + b
