# Sort the tuple in asscending order

tuple1=(21,12,13,16,17,18,45,78,89,67,8)
print("Original tuple:")
print(tuple1)

tuple2=list(tuple1)

for i in range(len(tuple2)):
    for j in range(i+1,len(tuple2)):
        if tuple2[i] < tuple2[j]:
            temp=tuple2[i]
            tuple2[i]=tuple2[j]
            tuple2[j]=temp

tuple3=tuple(tuple2)

print("Descending order in tuple:",tuple3)


