"""
Program: Find the Maximum Element in a Tuple

Description:
This program finds the largest element present in a tuple
without using Python's built-in max() function.

Example:
Input : (12, 13, 16, 17, 18, 45, 78, 89, 67, 8)
Output: 89

Author: Mayuri Bondge
Language: Python
"""

# Original tuple
numbers = (12, 13, 16, 17, 18, 45, 78, 89, 67, 8)

print("Original Tuple:")
print(numbers)

# Assume the first element is the maximum
maximum = numbers[0]

# Find the maximum element
for num in numbers:
    if num > maximum:
        maximum = num

# Display the result
print("Maximum Element in the Tuple:", maximum)