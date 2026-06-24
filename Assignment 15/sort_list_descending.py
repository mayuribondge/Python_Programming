"""
Program: Sort a List in Descending Order

Description:
This program sorts the elements of a list in descending order
using a simple comparison and swapping technique.

Example:
Input : [50, 20, 40, 10, 30]
Output: [50, 40, 30, 20, 10]

Author: Mayuri Bondge
Language: Python
"""

# Initialize the list
numbers = [50, 20, 40, 10, 30]

# Sort the list in descending order
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] < numbers[j]:
            # Swap elements
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

# Display the sorted list
print("List in Descending Order:", numbers)