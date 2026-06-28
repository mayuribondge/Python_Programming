"""
Program: Find the Intersection of Two Sets

Description:
This program finds the common elements (intersection)
between two sets without using Python's built-in
intersection() method. It compares each element of the
first set with every element of the second set using
nested loops and stores the matching elements in a new set.

Example:
Set 1 : {10, 20, 30, 40, 50, 60}
Set 2 : {70, 80, 90, 10, 20, 30}

Output:
{10, 20, 30}

Author: Mayuri Bondge
Language: Python
"""

# First set
set1 = {10, 20, 30, 40, 50, 60}

# Second set
set2 = {70, 80, 90, 10, 20, 30}

print("Set 1:", set1)
print("Set 2:", set2)

# Store common elements
intersection_set = set()

# Find the intersection using nested loops
for item1 in set1:
    for item2 in set2:
        if item1 == item2:
            intersection_set.add(item1)

# Display the result
print("Intersection of the Two Sets:", intersection_set)