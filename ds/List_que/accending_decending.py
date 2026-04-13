n = int(input("How many elements: "))

lst = []

for i in range(n):
    num = int(input("Enter number: "))
    lst.append(num)
print(lst)

lst.sort()
print(lst[-2])
# lst.reverse()
# print(lst)
