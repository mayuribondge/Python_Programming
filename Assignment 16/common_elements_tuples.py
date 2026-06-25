"""
Program: Find Common Elements in Two Tuples

Description:
This program finds and displays the common elements
present in two tuples.

Example:
Tuple 1 : (10, 20, 30, 40, 50)
Tuple 2 : (60, 70, 80, 30, 80, 10, 90)

Output:
10
30

Author: Mayuri Bondge
Language: Python
"""
# First tuple
tuple1 = (10, 20, 30, 40, 50)

# Second tuple
tuple2 = (60, 70, 80, 30, 80, 10, 90)

print("First Tuple:")
print(tuple1)

print("\nSecond Tuple:")
print(tuple2)

common_elements = []

for item1 in tuple1:
    for item2 in tuple2:
        if item1 == item2 and item1 not in common_elements:
            common_elements.append(item1)

print("Common Elements:", tuple(common_elements))