# Write a program to find the symmetric differnce of two set

set1={10,20,30,40,50,60}
set2={70,80,90,10,20,30}

print("Set 1:",set1)
print("Set 2:",set2)

result=set()

for i in set1:
    if i not in set2:
        result.add(i)

for i in set2:
    if i not in set1:
        result.add(i)

print("Symmentric differnce between two set:",result)


