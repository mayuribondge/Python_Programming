"""
Program: Find the Longest Word in a File

Description:
This program reads the contents of a text file, splits the
text into individual words, identifies the longest word,
and displays both the longest word and its length.

Example:
File Content:
Python is a powerful programming language

Output:
Longest Word: programming
Length: 11

Author: Mayuri Bondge
Language: Python
"""

# Open the file in read mode
file = open("file.txt", "r")

# Read the file content
data = file.read()

# Close the file
file.close()

# Split the content into words
words = data.split()

# Assume the first word is the longest
longest_word = words[0]

# Find the longest word
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

# Display the result
print("Longest Word in the File:", longest_word)
print("Length of the Longest Word:", len(longest_word))