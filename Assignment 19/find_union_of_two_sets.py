# Write a program to find the union of two set

Set1={10,20,30,40,50,60}
set2={70,80,90,10,30,20}
print("Set 1:",Set1)
print("Set 2:",set2)

result=set()

for i in Set1:
    result.add(i)

for i in set2:
    result.add(i)

print("Union of two set:",result)