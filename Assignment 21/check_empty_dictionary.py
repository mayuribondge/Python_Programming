"""
Program: Check Whether a Dictionary is Empty

Description:
This program checks whether a dictionary is empty without
using Python's built-in functions. It iterates through the
dictionary to determine whether any key-value pairs are
present and displays the appropriate result.

Example:
Input:
{}

Output:
Dictionary is empty.

Author: Mayuri Bondge
Language: Python
"""

# Create an empty dictionary
student = {}

print("Dictionary:")
print(student)

# Assume the dictionary is empty
is_not_empty = False

# Check if the dictionary contains any elements
for key in student:
    is_not_empty = True
    break

# Display the result
if is_not_empty:
    print("Dictionary is not empty.")
else:
    print("Dictionary is empty.")