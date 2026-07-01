"""
Program: Check Whether a Value Exists in a Dictionary

Description:
This program checks whether a user-specified value exists
in a dictionary without using Python's built-in methods.
It iterates through all dictionary values, compares each
value with the user input, and displays whether the value
is present or not.

Example:
Dictionary:
{'name': 'Mayuri', 'age': '12', 'marks': '90', 'city': 'Pune'}

Input:
Pune

Output:
Value exists in the dictionary.

Author: Mayuri Bondge
Language: Python
"""

# Create a dictionary
student = {
    "name": "Mayuri",
    "age": "12",
    "marks": "90",
    "city": "Pune"
}

print("Dictionary:")
print(student)

# Input value to search
search_value = input("Enter the value to search: ")

# Count matching values
count = 0

for value in student.values():
    if value == search_value:
        count += 1

# Display the result
if count > 0:
    print("Value exists in the dictionary.")
else:
    print("Value does not exist in the dictionary.")