n = int(input("How many elements n first list: "))
lst = []

for i in range(n):
    num = int(input("Enter number: "))
    lst.append(num)

print("there are first lst:",lst)
new= []

for i in lst:
        if i not in new:
            print(i,":",lst.count(i))
            new.append(i)
