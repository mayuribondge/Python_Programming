# Write a program to check whether one is superset of another

set1={10,20,30}
set2={10,20,30,40,50}

print("Set 1:",set1)
print("Set 2:",set2)

set3=set()

for i in set2:
    if i in set1:
        set3.add(i)

if set3==set1:
    print("One is superset of another:")
else:
    print("One is not superset of another:")
# print(set2.issuperset(set1))



