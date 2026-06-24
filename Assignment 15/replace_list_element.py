"""
Program: Replace an Element in a List

Description:
This program replaces a specified element in a list with
a new element entered by the user.

Example:
Original List : [5, 10, 15, 20, 25]
Replace : 15
New Value : 100
Updated List : [5, 10, 100, 20, 25]

Author: Mayuri Bondge
Language: Python
"""

numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60]

old_value = int(input("Enter the number to replace: "))
new_value = int(input("Enter the new number: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == old_value:
        numbers[i] = new_value
        found = True
        break

if found:
    print("Updated List:", numbers)
else:
    print("Element not found in the list.")