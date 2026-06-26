"""
Program: Find Non-Common Elements Between Two Tuples

Description:
This program finds the elements that are present in the first
tuple but not in the second tuple without using Python's
built-in set operations.

Example:
Tuple 1 : (10, 20, 30, 40, 50)
Tuple 2 : (60, 70, 80, 30, 80, 10, 90)

Output:
(20, 40, 50)

Author: Mayuri Bondge
Language: Python
"""

# First tuple
tuple1 = (10, 20, 30, 40, 50)

# Second tuple
tuple2 = (60, 70, 80, 30, 80, 10, 90)

print("First Tuple:")
print(tuple1)

print("Second Tuple:")
print(tuple2)

# Store non-common elements
result = ()

for i in range(len(tuple1)):
    if tuple1[i] not in tuple2:
        result = result + (tuple1[i],)

print("Elements present in Tuple 1 but not in Tuple 2:")
print(result)