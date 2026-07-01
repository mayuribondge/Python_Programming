"""
Program: Check Whether a Key Exists in a Dictionary

Description:
This program checks whether a user-specified key exists in
a dictionary without using Python's built-in methods. It
iterates through the dictionary keys and displays whether
the key is present or not.

Example:
Dictionary:
{'name': 'Mayuri', 'age': 12, 'marks': 90, 'city': 'Pune'}

Input:
age

Output:
Key exists in the dictionary.

Author: Mayuri Bondge
Language: Python
"""

# Create a dictionary
student = {
    "name": "Mayuri",
    "age": 12,
    "marks": 90,
    "city": "Pune"
}

print("Dictionary:")
print(student)

# Input key to search
search_key = input("Enter the key to search: ")

# Assume the key does not exist
found = False

# Search for the key
for key in student:
    if key == search_key:
        found = True
        break

# Display the result
if found:
    print("Key exists in the dictionary.")
else:
    print("Key does not exist in the dictionary.")