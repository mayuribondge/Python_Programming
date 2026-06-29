"""
Program: Find the Second Smallest Element in a Tuple

Description:
This program finds the second smallest element in a tuple
without using Python's built-in sorting functions. The tuple
is converted into a list, sorted in ascending order using
nested loops, and then converted back into a tuple. Finally,
the second smallest element is displayed.

Example:
Input : (21, 12, 13, 16, 17, 18, 45, 78, 89, 67, 8)
Output: 12

Author: Mayuri Bondge
Language: Python
"""

# Original tuple
tuple1 = (21, 12, 13, 16, 17, 18, 45, 78, 89, 67, 8)

print("Original Tuple:")
print(tuple1)

# Convert tuple to list
tuple2 = list(tuple1)

# Sort the list in ascending order
for i in range(len(tuple2)):
    for j in range(i + 1, len(tuple2)):
        if tuple2[i] > tuple2[j]:
            temp = tuple2[i]
            tuple2[i] = tuple2[j]
            tuple2[j] = temp

# Convert list back to tuple
tuple3 = tuple(tuple2)

# Display the second smallest element
print("Second Smallest Element in the Tuple:", tuple3[1])