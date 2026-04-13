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

temp=lst1.copy()
new=[]
for i in lst:
    if i in temp:
        new.append(i)
        temp.remove(i)

print("there are common elements in two lists: ",new)

zec = lst + lst1