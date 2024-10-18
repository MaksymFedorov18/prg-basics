# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = int(input("Enter number: "))
number2 = int(input("Enter second number: "))
operator = input("Enter the operator to execute the function: ")
result = 0

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2 
elif operator == "/":
    result = number1 / number2

print(f'Result is {result}')