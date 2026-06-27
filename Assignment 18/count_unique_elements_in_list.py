"""
Program: Count the Number of Unique Elements in a List

Description:
This program counts the number of unique elements in a list
by converting the list into a set. Since sets store only
unique values, duplicate elements are automatically removed.

Example:
Input : [10, 20, 30, 10, 20, "Apple", "Apple"]
Output:
Unique Elements: {10, 20, 30, "Apple"}
Count: 4

Author: Mayuri Bondge
Language: Python
"""

# Original list
list1 = [10, 0, 30, 40, 50, 60, 10, 20, 30, "Mayuri", "Mango", "Mayuri"]

print("Original List:")
print(list1)

# Convert list to set
unique_elements = set(list1)

# Count unique elements
count = 0

for item in unique_elements:
    count += 1

# Display the result
print("Unique Elements:", unique_elements)
print("Number of Unique Elements:", count)