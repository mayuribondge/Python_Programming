"""
Program: Count Uppercase and Lowercase Letters Separately

Description:
This program counts the number of uppercase and lowercase
letters in a user-entered string.

Author: Mayuri Bondge
Language: Python
"""

# Take input from the user
string = input("Enter a string: ")

# Initialize counters
lower_count = 0
upper_count = 0

# Count uppercase and lowercase letters
for char in string:
    if 'A' <= char <= 'Z':
        upper_count += 1
    elif 'a' <= char <= 'z':
        lower_count += 1

# Display the results
print("\n----- Result -----")
print("Lowercase letters :", lower_count)
print("Uppercase letters :", upper_count)