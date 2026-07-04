"""
Program: Divide Two Numbers with Exception Handling

Description:
This program divides two numbers entered by the user and
handles possible exceptions such as invalid input and
division by zero. It also uses a generic exception handler
to catch any unexpected errors and a finally block to
indicate the end of program execution.

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
    # Input numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Perform division
    result = num1 / num2

    # Display result
    print("Result:", result)

except ValueError:
    print("Error: Please enter valid integer values.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except Exception as error:
    print("Unexpected Error:", error)

finally:
    print("Program Ended.")