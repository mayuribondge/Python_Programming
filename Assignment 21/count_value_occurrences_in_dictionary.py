# Count how many times particular value appear

dict1={"name":"Mayuri","age":"12","marks":"90","city":"Pune","Age":"12"}
print(dict1)

value=input("Enter a value:")

count=0

for i in dict1.values():
    if i==value:
        count=count+1

print(count)