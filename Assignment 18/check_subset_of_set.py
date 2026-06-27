"""
Program: Check Whether One Set is a Subset of Another

Description:
This program checks whether the first set is a subset of the
second set without using Python's built-in issubset() method.
It compares the elements of the first set with the second set
and determines whether all elements are present.

Example:
Set 1 : {10, 20, 30, 40, 50, 60}
Set 2 : {70, 80, 90, 10, 20, 30, 40, 50, 60}

Output:
Set 1 is a subset of Set 2.

Author: Mayuri Bondge
Language: Python
"""

# First set
set1 = {10, 20, 30, 40, 50, 60}

# Second set
set2 = {70, 80, 90, 10, 20, 30, 40, 50, 60}

print("Set 1:", set1)
print("Set 2:", set2)

# Store common elements
common_elements = set()

# Find common elements
for item in set1:
    if item in set2:
        common_elements.add(item)

# Check if Set 1 is a subset of Set 2
if set1 == common_elements:
    print("Set 1 is a subset of Set 2.")
else:
    print("Set 1 is not a subset of Set 2.")