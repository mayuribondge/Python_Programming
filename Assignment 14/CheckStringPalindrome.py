"""
Program: Check Whether a String is Palindrome or Not

Description:
This program checks whether a user-entered string is a palindrome.
A palindrome is a string that reads the same forward and backward.

Examples:
- madam → Palindrome
- level → Palindrome
- python → Not a palindrome

Author: Mayuri Bondge
Language: Python
"""

# Take input from the user
string = input("Enter a string: ")

# Initialize an empty string to store the reverse
reverse = ""

# Reverse the string using a loop
for char in string:
    reverse = char + reverse

# Check if the original string and reversed string are the same
if string == reverse:
    print("\nResult: The string is a palindrome.")
else:
    print("\nResult: The string is not a palindrome.")
