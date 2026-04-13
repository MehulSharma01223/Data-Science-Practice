n = int(input("How many elements: "))

lst = []

for i in range(n):
    num = int(input("Enter number: "))
    lst.append(num)
print(lst)
c= sum(lst)/n
print("average of list is ",c)

print((lst[::-1]))
# print(lst.reverse())