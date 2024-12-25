# simple-calculator
A simple command-line calculator written in Python. This program allows users to perform basic arithmetic operations: addition, subtraction, multiplication, and division.

A **function** is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
In Python a function is defined using the **def** keyword

## Features

- **Addition**: Add two numbers.
- **Subtraction**: Subtract one number from another.
- **Multiplication**: Multiply two numbers.
- **Division**: Divide one number by another (handles division by zero).

## How to Use

1. Clone or download the repository.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script using Python:
   ```bash
   python calculator.py
   ```
4. Follow the prompts:
   - Enter the first number.
   - Enter the second number.
   - Choose an operator from the menu:
     - `1` for addition
     - `2` for subtraction
     - `3` for multiplication
     - `4` for division
   - The result will be displayed.

## Example Usage

```plaintext
Enter first number: 10
Enter second number: 5
Operator: 
[1] Addition
[2] Subtraction
[3] Multiplication
[4] Division
Choose an operator: 1
Sum: 10 + 5 = 15
```

## Code Overview

The main functionalities are implemented through the following functions:

- `add(x, y)`: Returns the sum of `x` and `y`.
- `subtract(x, y)`: Returns the difference between `x` and `y`.
- `multiply(x, y)`: Returns the product of `x` and `y`.
- `division(x, y)`: Returns the quotient of `x` divided by `y` or a message if `y` is 0.

The `calculator()` function serves as the main interface, prompting the user for inputs and displaying the results based on the selected operation.
