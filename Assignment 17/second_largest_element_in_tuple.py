"""
Program: Find the Second Largest Element in a Tuple

Description:
This program finds the second largest element in a tuple
without using Python's built-in sorting functions. The tuple
is first converted into a list, sorted in ascending order
using comparison and swapping, and then converted back into
a tuple.

Example:
Input : (21, 12, 13, 16, 17, 18, 45, 78, 89, 67, 8)
Output: 78

Author: Mayuri Bondge
Language: Python
"""

# Original tuple
numbers = (21, 12, 13, 16, 17, 18, 45, 78, 89, 67, 8)

print("Original Tuple:")
print(numbers)

# Convert tuple to list
numbers_list = list(numbers)

# Sort the list in ascending order
for i in range(len(numbers_list)):
    for j in range(i + 1, len(numbers_list)):
        if numbers_list[i] > numbers_list[j]:
            temp = numbers_list[i]
            numbers_list[i] = numbers_list[j]
            numbers_list[j] = temp

# Convert list back to tuple
sorted_tuple = tuple(numbers_list)

# Display the second largest element
print("Second Largest Element in the Tuple:", sorted_tuple[-2])