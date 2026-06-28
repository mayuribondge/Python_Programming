# Write a program to count the number of unique elements in list

list1=[10,0,30,40,50,60,10,20,30,"Maayuri","Mango","Maayuri"]

print("Original list:")
print(list1)

set1=set(list1)

count=0

for i in set1:
    count=count+1

print("unique elements in list:",count)
print("unique element in list:",set1)