# String-Based Exceptions, Class-Based Exceptions, and Nesting Exception Handlers Examples

# 1. String-Based Exceptions
try:
    num1 = 10
    num2 = 0
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Division by zero")

# 2. Class-Based Exceptions
class MyCustomError(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise MyCustomError("This is a custom error")
except MyCustomError as e:
    print("Error:", e.message)

# 3. Nesting Exception Handlers
try:
    try:
        num = int(input("Enter a number: "))
        result = 10 / num
    except ValueError:
        print("Invalid input")
    except ZeroDivisionError:
        print("Error: Division by zero")
except Exception as e:
    print("Exception:", e)
