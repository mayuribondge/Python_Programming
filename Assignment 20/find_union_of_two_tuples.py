"""
Program: Find the Union of Two Tuples

Description:
This program finds the union of two tuples without using
Python's built-in set union() method. It combines the
elements of both tuples into a list while ensuring that
duplicate elements are not added. Finally, the list is
converted into a tuple.

Example:
Tuple 1 : (10, 20, 30, 40, 50)
Tuple 2 : (30, 40, 60, 70, 80)

Output:
(10, 20, 30, 40, 50, 60, 70, 80)

Author: Mayuri Bondge
Language: Python
"""

# First tuple
tuple1 = (10, 20, 30, 40, 50)

# Second tuple
tuple2 = (30, 40, 60, 70, 80)

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)

# Store the union
result = []

# Add elements from the first tuple
for item in tuple1:
    if item not in result:
        result.append(item)

# Add elements from the second tuple
for item in tuple2:
    if item not in result:
        result.append(item)

# Convert list to tuple
union_tuple = tuple(result)

print("Union of the Two Tuples:", union_tuple)