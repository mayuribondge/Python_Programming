"""
Program: Display Message Multiple Times

Description:
    This program accepts a number and displays the message
    "Jay Ganesh..." the specified number of times.

Concepts:
    - Functions
    - for Loop
    - range()
    - Function Calling
    - main() Function

Author: Mayuri Bondge
"""


def Display(num):
    for i in range(0, num):
        print("Jay Ganesh...")


def main():
    Display(2)


if __name__ == "__main__":
    main()