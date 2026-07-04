"""
Program: Simple Calculator with Exception Handling

Description:
This program performs basic arithmetic operations such as
addition, subtraction, multiplication, division, and floor
division. It uses exception handling to manage invalid
numeric input and division by zero, ensuring that the
program executes safely without crashing.

Example:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Floor Division

Author: Mayuri Bondge
Language: Python
"""

try:
    # Input numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Display menu
    print("\n----- Calculator Menu -----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")

    choice = int(input("Enter your choice: "))

    # Perform operation
    if choice == 1:
        result = num1 + num2
        print("Addition:", result)

    elif choice == 2:
        result = num1 - num2
        print("Subtraction:", result)

    elif choice == 3:
        result = num1 * num2
        print("Multiplication:", result)

    elif choice == 4:
        result = num1 / num2
        print("Division:", result)

    elif choice == 5:
        result = num1 // num2
        print("Floor Division:", result)

    else:
        print("Invalid choice! Please select between 1 and 5.")

except ValueError:
    print("Error: Please enter valid numeric values.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

finally:
    print("Program Ended.")