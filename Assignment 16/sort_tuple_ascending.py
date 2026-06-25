"""
Program: Sort a Tuple in Ascending Order

Description:
This program sorts the elements of a tuple in ascending order.
Since tuples are immutable, the tuple is first converted into a list,
sorted using comparison and swapping, and then converted back to a tuple.

Example:
Input : (21, 12, 13, 16, 17)
Output: (12, 13, 16, 17, 21)

Author: Mayuri Bondge
Language: Python
"""

# Original tuple
tuple1 = (21, 12, 13, 16, 17, 18, 45, 78, 89, 67, 8)

print("Original Tuple:")
print(tuple1)

# Convert tuple to list
tuple_list = list(tuple1)

# Sort in ascending order
for i in range(len(tuple_list)):
    for j in range(i + 1, len(tuple_list)):
        if tuple_list[i] > tuple_list[j]:
            temp = tuple_list[i]
            tuple_list[i] = tuple_list[j]
            tuple_list[j] = temp

# Convert list back to tuple
sorted_tuple = tuple(tuple_list)

print("Ascending Order Tuple:", sorted_tuple)