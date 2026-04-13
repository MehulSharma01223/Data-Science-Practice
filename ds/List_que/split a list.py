n = int(input("How many elements: "))

lst = []

for i in range(n):
    num = int(input("Enter number: "))
    lst.append(num)
print(lst)

mid = len(n)//2
print("first half",lst[mid:])
print("second  half",lst[:mid])