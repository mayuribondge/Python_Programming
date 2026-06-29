"""
Program: Find the Index of a Given Element in a Tuple

Description:
This program finds the index of a user-specified element
in a tuple without using Python's built-in index() method.
It searches each element sequentially and displays the
index if the element is found.

Example:
Tuple : (12, 13, 16, 17, 18, 45, 78, 89, 67)
Input : 45
Output: Index = 5

Author: Mayuri Bondge
Language: Python
"""

# Original tuple
tuple1 = (12, 13, 16, 17, 18, 45, 78, 89, 67)

# Input element
element = int(input("Enter the element to find its index: "))

# Search for the element
found = False

for i in range(len(tuple1)):
    if tuple1[i] == element:
        print("Index of the element:", i)
        found = True
        break

# Element not found
if not found:
    print("Element not found in the tuple.")