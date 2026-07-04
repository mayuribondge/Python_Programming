"""
Program: Simple ATM System with Exception Handling

Description:
This program simulates a simple ATM system using exception
handling. It allows the user to check the account balance,
deposit money, and withdraw money. The program validates
user input, prevents invalid transactions such as negative
amounts and insufficient balance, and handles runtime
errors using try-except blocks.

Example:
1. Check Balance
2. Deposit Money
3. Withdraw Money

Author: Mayuri Bondge
Language: Python
"""

# Initial account balance
balance = 10000

try:
    print("========== ATM MENU ==========")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")

    choice = int(input("Enter your choice: "))

    # Check balance
    if choice == 1:
        print("Available Balance:", balance)

    # Deposit money
    elif choice == 2:
        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        balance += amount
        print("Deposit Successful.")
        print("Updated Balance:", balance)

    # Withdraw money
    elif choice == 3:
        withdraw = float(input("Enter withdrawal amount: "))

        if withdraw <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        if withdraw > balance:
            raise Exception("Insufficient balance.")

        balance -= withdraw
        print("Withdrawal Successful.")
        print("Remaining Balance:", balance)

    else:
        print("Invalid choice. Please select a valid option.")

except ValueError as error:
    print("Value Error:", error)

except Exception as error:
    print("Error:", error)

finally:
    print("Thank you for using our ATM!")