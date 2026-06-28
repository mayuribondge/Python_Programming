"""
Program: Remove Duplicate Elements from a List Using a Set

Description:
This program removes duplicate elements from a list by
converting the list into a set. Since sets store only
unique values, all duplicate elements are automatically
removed.

Example:
Input : [10, 20, 30, 40, "Mango", "Mango", "Apple", 10, 20]

Output:
{40, 10, 'Apple', 'Mango', 20, 30}

Author: Mayuri Bondge
Language: Python
"""

# Original list
list1 = [10, 20, 30, 40, "Mango", "Mango", "Apple", 10, 20, 30, 40, 50]

print("Original List:")
print(list1)

# Convert the list into a set
unique_elements = set(list1)

# Display the result
print("List After Removing Duplicates:")
print(unique_elements)