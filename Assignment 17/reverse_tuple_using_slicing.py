"""
Program: Reverse a Tuple Using Slicing

Description:
This program reverses the elements of a tuple using Python's
slicing technique. The slice operator [::-1] creates a new
tuple with all elements in reverse order.

Example:
Input : (12, 13, 16, 17, 18, 45, 78, 89, 67)
Output: (67, 89, 78, 45, 18, 17, 16, 13, 12)

Author: Mayuri Bondge
Language: Python
"""

# Original tuple
numbers = (12, 13, 16, 17, 18, 45, 78, 89, 67)

# Reverse the tuple using slicing
reversed_tuple = numbers[::-1]

# Display the results
print("Original Tuple:", numbers)
print("Reversed Tuple:", reversed_tuple)