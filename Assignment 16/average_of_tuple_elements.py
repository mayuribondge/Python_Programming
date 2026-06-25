"""
Program: Find the Average of Elements in a Tuple

Description:
This program calculates the sum, count, and average
of all elements present in a tuple.

Example:
Input : (12, 13, 16, 17, 18)
Output:
Sum     : 76
Count   : 5
Average : 15.2

Author: Mayuri Bondge
Language: Python
"""

# Original tuple
numbers = (12, 13, 16, 17, 18, 45, 78, 89, 67, 8)

print("Original Tuple:")
print(numbers)

# Initialize variables
total = 0
count = 0

# Calculate sum and count
for num in numbers:
    total += num
    count += 1

# Calculate average
average = total / count

# Display results
print("\nSum of all elements:", total)
print("Number of elements:", count)
print("Average of all elements:", average)