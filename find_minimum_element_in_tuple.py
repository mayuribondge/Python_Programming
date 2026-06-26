"""
Program: Find the Minimum Element in a Tuple

Description:
This program finds the smallest element in a tuple without
using Python's built-in min() function. It compares each
element with the current minimum value and updates it
whenever a smaller element is found.

Example:
Input : (12, 13, 16, 17, 18, 45, 78, 89, 67, 8)
Output: 8

Author: Mayuri Bondge
Language: Python
"""

# Original tuple
numbers = (12, 13, 16, 17, 18, 45, 78, 89, 67, 8)

print("Original Tuple:")
print(numbers)

# Assume the first element is the minimum
minimum = numbers[0]

# Find the minimum element
for num in numbers:
    if num < minimum:
        minimum = num

# Display the result
print("Minimum Element in the Tuple:", minimum)