"""
Program: Count the Number of Characters in a File

Description:
This program reads the contents of a text file and counts
the total number of characters present in it. It opens the
file in read mode, reads all the data, calculates the
character count using the len() function, and displays the
result.

Example:
File Content:
Hello World

Output:
Number of Characters: 11

Author: Mayuri Bondge
Language: Python
"""

# Open the file in read mode
file = open("file.txt", "r")

# Read the file content
data = file.read()

# Count the number of characters
character_count = len(data)

# Display the result
print("Number of Characters in the File:", character_count)

# Close the file
file.close()