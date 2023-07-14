global_var = 10

def my_function():
    local_var = 20
    print("Local variable:", local_var)
    print("Global variable within function:", global_var)

my_function()

print("Global variable outside function:", global_var)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = 5
result = factorial(num)
print("Factorial of", num, "is", result)

def modify_list(my_list):
    my_list.append(4)
    my_list[1] = 100

numbers = [1, 2, 3]
print("Original List:", numbers)

modify_list(numbers)
print("Modified List:", numbers)
