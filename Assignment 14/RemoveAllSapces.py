"""
Program: Remove All Spaces from a String

Description:
This program removes all spaces from a user-entered string
without using the replace() function.

Example:
Input : Hello World Python
Output: HelloWorldPython

Author: Mayuri Bondge
Language: Python
"""

# Take input from the user
string = input("Enter a string: ")

# Initialize an empty string
result = ""

# Traverse each character
for char in string:
    if char != " ":
        result += char

# Display the result
print("\nString after removing spaces:", result)
