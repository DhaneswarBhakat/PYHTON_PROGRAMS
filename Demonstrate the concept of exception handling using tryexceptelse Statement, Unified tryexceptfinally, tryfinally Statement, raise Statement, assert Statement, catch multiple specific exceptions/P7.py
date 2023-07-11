# Exception Handling Examples

# 1. try/except/else Statement
try:
    num1 = 10
    num2 = 0
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Division by zero")
else:
    print("Result:", result)

# 2. Unified try/except/finally
try:
    file = open("nonexistent_file.txt", "r")
    content = file.read()
except FileNotFoundError as e:
    print("Error:", e)
finally:
    if 'file' in locals() or 'file' in globals():
        file.close()

# 3. try/finally Statement
try:
    num = int(input("Enter a number: "))
finally:
    print("Finally block executed")

# 4. raise Statement
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age > 120:
        raise ValueError("Invalid age")
    else:
        print("Valid age")

try:
    check_age(-5)
except ValueError as e:
    print("Error:", e)

# 5. assert Statement
def divide(num1, num2):
    assert num2 != 0, "Division by zero"
    return num1 / num2

try:
    result = divide(10, 0)
except AssertionError as e:
    print("Error:", e)

# 6. Catching multiple specific exceptions
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except (ValueError, ZeroDivisionError):
    print("Error: Invalid input or division by zero")
