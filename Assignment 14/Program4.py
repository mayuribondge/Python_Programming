# Write a program to remove duplicate words in sentence

String=input("Enter a string:")

save=""

for i in String:
    if i not in save:
        save=save+i

print("After removing duplicate:",save)





