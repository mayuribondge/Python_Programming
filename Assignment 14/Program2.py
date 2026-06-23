"""
Program: Find the Longest Word in a Sentence

Description:
This program finds the longest word in a user-entered sentence
without using the split() function.

Example:
Input : Python is an amazing programming language
Output: programming

Author: Mayuri Bondge
Language: Python
"""

# Take input from the user
string = input("Enter a sentence: ")

# Initialize variables
word = ""
longest = ""

# Traverse each character
for char in string:
    if char != " ":
        word += char
    else:
        if len(word) > len(longest):
            longest = word
        word = ""

# Check the last word (since there is no space after it)
if len(word) > len(longest):
    longest = word

# Display the result
print("\nLongest word:", longest)