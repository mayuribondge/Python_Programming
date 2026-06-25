"""
Program: Check Whether a Tuple is Sorted or Not

Description:
This program checks whether the elements of a tuple
are arranged in ascending order.

Example:
Input : (10, 20, 30, 40, 50)
Output: Tuple is sorted in ascending order

Author: Mayuri Bondge
Language: Python
"""

# Original tuple
numbers = (10, 20, 30, 40, 50)

print("Original Tuple:")
print(numbers)

# Assume the tuple is sorted
is_sorted = True

# Check each element with the next element
for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        is_sorted = False
        break

# Display result
if is_sorted:
    print("Tuple is sorted in ascending order.")
else:
    print("Tuple is not sorted.")