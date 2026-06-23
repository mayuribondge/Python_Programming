"""
Program: Remove Duplicate Words from a Sentence

Description:
This program removes duplicate words from a sentence
without using the split() function.

Example:
Input : this is is a python python program
Output: this is a python program

Author: Mayuri Bondge
Language: Python
"""

# Take input from the user
string = input("Enter a sentence: ")

word = ""
result = ""
visited = []

# Traverse each character
for char in string + " ":
    if char != " ":
        word += char
    else:
        if word not in visited:
            visited.append(word)
            result += word + " "
        word = ""

# Display the result
print("\nSentence after removing duplicate words:")
print(result.strip())
