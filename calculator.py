#My calculator project
num1 = eval(input("Enter first_number:"))
num2 = eval(input("Enter second_number:"))

operator = input("Enter operator:")
def add(num1, num2):
    result = num1 + num2
    return result

def subtract(num1, num2):
    result = num1 - num2
    return result

def divide(num1, num2):
    result = num1 / num2
    return result

def multiply(num1, num2):
    result = num1 * num2
    return result
    