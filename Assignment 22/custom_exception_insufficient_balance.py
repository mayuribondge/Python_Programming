"""
Program: Custom Exception for Insufficient Balance

Description:
This program demonstrates how to create and use a custom
exception in Python. It checks whether the account balance
meets the minimum required balance. If the balance is less
than ₹30,000, a custom exception named InsufficientBalance
is raised; otherwise, a success message is displayed.

Example:
Input : 25000

Output:
Error: Minimum balance should be ₹30,000.

Author: Mayuri Bondge
Language: Python
"""

# Custom exception class
class InsufficientBalance(Exception):
    pass

try:
    # Input account balance
    balance = int(input("Enter your account balance: "))

    # Check minimum balance
    if balance < 30000:
        raise InsufficientBalance("Minimum balance should be ₹30,000.")

    print("Balance is sufficient.")

except InsufficientBalance as error:
    print("Error:", error)