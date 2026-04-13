Name = input("ENter a your name :- ")

count= 0

for i in Name:
    if i in "aeiouAEIUO":
        count= count+1

print("number of vowels:",count)