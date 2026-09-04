"""
Program: Check Whether a Number is Prime

Description:
    This program checks whether a given number is prime or not.
    The program uses a loop to check if the number is divisible
    by any number between 2 and num - 1.

Concepts:
    - Functions
    - for Loop
    - range()
    - Modulus Operator
    - Conditional Statements
    - Boolean Values
    - break Statement
    - User Input

Author: Mayuri Bondge
"""


def CheckPrime(num):
    if num < 2:
        return False

    Count = 0

    for i in range(2, num):
        if num % i == 0:
            Count = Count + 1
            break

    if Count == 0:
        return True
    else:
        return False


def main():
    num = int(input("Enter a number: "))

    ret = CheckPrime(num)

    if ret:
        print("Number is prime")
    else:
        print("Number is not prime")


if __name__ == "__main__":
    main()