"""
Program: Display the Last Five Lines of a File

Description:
This program reads a text file and displays the last five
lines. It uses the readlines() method to read all lines
into a list and then uses list slicing to retrieve and
print the last five lines.

Example:
File Content:
Line 1
Line 2
...
Line 10

Output:
Line 6
Line 7
Line 8
Line 9
Line 10

Author: Mayuri Bondge
Language: Python
"""

# Open the file in read mode
file = open("file.txt", "r")

# Read all lines from the file
lines = file.readlines()

# Display the last five lines
print("Last Five Lines of the File:")

for line in lines[-5:]:
    print(line, end="")

# Close the file
file.close()