"""
Program: Copy the Contents of One File into Another

Description:
This program copies the contents of one text file into
another file. It opens the source file in read mode,
reads its contents, writes them into the destination
file, and closes both files.

Example:
Source File : file.txt
Destination File : myfile.txt

Author: Mayuri Bondge
Language: Python
"""

# Open the source file
file1 = open("file.txt", "r")

# Open the destination file
file2 = open("myfile.txt", "w")

# Read the content of the source file
data = file1.read()

# Write the content into the destination file
file2.write(data)

print("File copied successfully.")

# Close both files
file1.close()
file2.close()