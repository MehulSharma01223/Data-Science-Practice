n = int(input("How many elements: "))

lst = []

for i in range(n):
    num = int(input("Enter number: "))
    lst.append(num)
print(lst)
lst.sort()
print("there second largest num in lst is :",lst[-2])