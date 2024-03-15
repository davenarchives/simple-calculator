def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot be divided by zero"

def calculator():

    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    print("Operator: ")
    print("[1] Addition")
    print("[2] Subtraction")
    print("[3] Multiplication")
    print("[4] Division")

    operator = input("Choose an operator: ")

    if operator == '1':
        print(f"Sum: {x} + {y} = ", add(x, y))

    elif operator == '2':
        print(f"Difference: {x} - {y} = ", subtract(x, y))

    elif operator == '3':
        print(f"Product: {x} * {y} = ", multiply(x, y))

    elif operator == '4':
        print(f"Quotient: {x} / {y} = ", division(x, y))

    else:
        print("Invalid Input!")
calculator()
