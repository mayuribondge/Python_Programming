"""
Program: Use of Else Block with Try and Except

Description:
This program demonstrates the use of the else block with
try and except statements. It divides two numbers entered
by the user. If no exception occurs, the else block
executes and displays the result. If an invalid input or
division by zero occurs, the corresponding exception is
handled gracefully.

Example:
Input:
First Number : 20
Second Number: 5

Output:
Result: 4.0

Author: Mayuri Bondge
Language: Python
"""

try:
    # Input two numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Perform division
    result = num1 / num2

except ValueError:
    print("Error: Please enter valid integer values.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

else:
    # Executes only if no exception occurs
    print("Result:", result)