"""
Program: Check if Two Sets are Disjoint

Description:
This program checks whether two sets are disjoint.
Two sets are called disjoint if they do not have any
common elements.

Example:
Set 1 : {10, 20, 30}
Set 2 : {40, 50}
Output: Sets are disjoint.

Author: Mayuri Bondge
Language: Python
"""

# First set
set1 = {10, 20, 30}

# Second set
set2 = {40, 50}

print("Set 1:", set1)
print("Set 2:", set2)

# Assume the sets are disjoint
is_disjoint = True

# Check for common elements
for item in set1:
    if item in set2:
        is_disjoint = False
        break

# Display the result
if is_disjoint:
    print("Sets are disjoint.")
else:
    print("Sets are not disjoint.")