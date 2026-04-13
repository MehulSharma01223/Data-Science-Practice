n = int(input("How many elements: "))

lst = []

for i in range(n):
    num = int(input("Enter number: "))
    lst.append(num)
print(lst)
new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(i)

print(new_lst)