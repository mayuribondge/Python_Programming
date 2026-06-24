"""
Program: Sort a List in Ascending Order

Description:
This program sorts the elements of a list in ascending order
using a simple sorting technique (comparison and swapping).

Example:
Input : [50, 20, 40, 10, 30]
Output: [10, 20, 30, 40, 50]

Author: Mayuri Bondge
Language: Python
"""

# Initialize the list
numbers = [50, 20, 40, 10, 30]

# Sort the list in ascending order
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            # Swap elements
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

# Display the sorted list
print("List in Ascending Order:", numbers)

