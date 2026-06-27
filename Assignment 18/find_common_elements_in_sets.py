"""
Program: Find Common Elements in Two Sets

Description:
This program finds the common elements present in two sets
without using Python's built-in intersection() method. It
compares each element of the first set with the second set
and stores the matching elements in a new set.

Example:
Set 1 : {10, 20, 30}
Set 2 : {10, 20, 30, 40, 50}

Output:
{10, 20, 30}

Author: Mayuri Bondge
Language: Python
"""

# First set
set1 = {10, 20, 30}

# Second set
set2 = {10, 20, 30, 40, 50}

print("Set 1:", set1)
print("Set 2:", set2)

# Store common elements
common_elements = set()

# Find common elements
for item in set1:
    if item in set2:
        common_elements.add(item)

# Display the result
print("Common Elements:", common_elements)