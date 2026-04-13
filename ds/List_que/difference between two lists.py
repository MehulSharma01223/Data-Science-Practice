n = int(input("How many elements n first list: "))
m = int(input("how many elements in second list: "))
lst1 = []
lst = []

for i in range(n):
    num = int(input("Enter number: "))
    lst.append(num)

for i in range(m):
    nu = int(input("Enter number"))
    lst1.append(nu)
print("there are first lst:",lst)
print("there are second lst :",lst1)

new = []
for i in lst:
    if i not in lst1:
        new.append(i)

print("there are difference two list:",new)
