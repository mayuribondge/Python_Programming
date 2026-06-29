"""
Program: Find the Sum of All Elements in a Tuple

Description:
This program calculates the sum of all elements in a tuple
without using Python's built-in sum() function. It iterates
through each element of the tuple, adds it to a running total,
and displays the final sum.

Example:
Input : (12, 13, 16, 17, 18, 45, 78, 89, 67, 8)
Output: 363

Author: Mayuri Bondge
Language: Python
"""

# Original tuple
tuple1 = (12, 13, 16, 17, 18, 45, 78, 89, 67, 8)

print("Original Tuple:")
print(tuple1)

# Initialize sum
total = 0

# Calculate the sum of all elements
for i in range(len(tuple1)):
    total = total + tuple1[i]

# Display the result
print("Sum of All Elements in the Tuple:", total)