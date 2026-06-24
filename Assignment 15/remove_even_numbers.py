# Write a program to remove all even numbers from list

List=[11,12,13,4,15,16,46,78]
New_List=[]

for i in List:
    if i%2!=0:
        New_List.append(i)

print("Orginal List:",List)
print("After removing even numbers:",New_List)
