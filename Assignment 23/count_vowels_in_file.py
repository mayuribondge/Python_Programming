"""
Program: Count the Number of Vowels in a File

Description:
This program reads the contents of a text file and counts
the total number of vowels present in it. It checks both
uppercase and lowercase vowels while ignoring all other
characters.

Example:
File Content:
Hello World

Output:
Number of Vowels: 3

Author: Mayuri Bondge
Language: Python
"""

# Open the file in read mode
file = open("file.txt", "r")

# Read the file content
data = file.read()

# Initialize vowel counter
vowel_count = 0

# Count vowels
for character in data:
    if character in "aeiouAEIOU":
        vowel_count += 1

# Display the result
print("Number of Vowels in the File:", vowel_count)

# Close the file
file.close()