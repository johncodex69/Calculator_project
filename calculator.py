#My calculator project
num1 = eval(input("Enter first_number:"))
num2 = eval(input("Enter second_number:"))

operator = input("Enter operator:")
def add(num1, num2):
    result = num1 + num2
    print(result)

def subtract(num1, num2):
    result = num1 - num2
    print(result)

def divide(num1, num2):
    result = num1 / num2
    print(result)

def multiply(num1, num2):
    result = num1 * num2
    print(result)

#Checking operator
 
if operator == "+":
    add(num1, num2)
elif operator == "-":
    subtract(num1, num2)
elif operator == "/":
    divide(num1, num2)
elif operator == "*":
    multiply(num1, num2)

elif operator == "X" or operator == "x" or operator == "*":
    multiply(num1, num2)

else:
    print("Invalid operator")