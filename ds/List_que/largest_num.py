n = int(input("How many elements: "))

lst = []

for i in range(n):
    num = int(input("Enter number: "))
    lst.append(num)

print(max(lst))
print(min(lst))
print(sum(lst))
