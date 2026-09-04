"""
Program: Calculate Factorial of a Number

Description:
    This program accepts a number from the user and calculates
    its factorial using a for loop.

Concepts:
    - Functions
    - for Loop
    - range()
    - Multiplication
    - User Input
    - Return Statement

Author: Mayuri Bondge
"""


def CalculateFactorial(No):
    Fact = 1

    for i in range(1, No + 1):
        Fact = Fact * i

    return Fact


def main():
    No = int(input("Enter your number: "))

    Ret = CalculateFactorial(No)

    print("Factorial is:", Ret)


if __name__ == "__main__":
    main()