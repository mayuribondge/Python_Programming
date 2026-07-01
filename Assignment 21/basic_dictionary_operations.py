"""
Program: Basic Dictionary Operations in Python

Description:
This program demonstrates the basic operations that can be
performed on a dictionary. It includes creating a dictionary,
accessing keys and values, retrieving values using keys,
adding new key-value pairs, updating existing values,
deleting keys, removing the last inserted item, and counting
the total number of key-value pairs.

Example:
Dictionary:
{'name': 'Mayuri', 'age': 12, 'marks': 90}

Author: Mayuri Bondge
Language: Python
"""

# Create a dictionary
student = {
    "name": "Mayuri",
    "age": 12,
    "marks": 90
}

print("Original Dictionary:")
print(student)

# Print all keys
print("\nDictionary Keys:")
print(student.keys())

# Print all values
print("\nDictionary Values:")
print(student.values())

# Access value using key
print("\nAge:", student["age"])

# Add a new key-value pair
student["city"] = "Pune"
print("\nAfter Adding a New Key:")
print(student)

# Update an existing value
student["age"] = 21
print("\nAfter Updating Age:")
print(student)

# Delete a specific key
del student["age"]
print("\nAfter Deleting 'age' Key:")
print(student)

# Remove the last inserted item
student.popitem()
print("\nAfter Removing Last Inserted Item:")
print(student)

# Count key-value pairs
count = 0

for key in student:
    count += 1

print("\nNumber of Key-Value Pairs:", count)