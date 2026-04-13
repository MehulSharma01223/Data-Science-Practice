n = int(input("How many elements: "))

lst = []

for i in range(n):
    num = int(input("Enter number: "))
    lst.append(num)
print(lst)

checked = []
for i in lst :
    if i not in checked:
        print(i,":",lst.count(i))
        checked.append(i)  