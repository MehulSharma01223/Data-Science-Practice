# Day 1

# Q1: Remove duplicates
arr = [1,2,2,3,4,4]
unique = []

for i in arr:
    if i not in unique:
        unique.append(i)

print(unique)

# Q2:  (1) Common elements
#      (2) Elements presents in A not in B

A = [1,2,3,4,5]
B = [3,4,5,6,7]
common = []
new = []
for i in  A:
    if i in B:
        if i not in common :
            common.append(i)
        else :
            new.append(i)
print("common:",common)
print("A not in B:",new)

# Q3. (1)Extract all elements divisible by 10
#     (2)Replace elements greater than 20 with 0
#     (3)Find cumulative sum of the modified array

# (1) Extract all elements divisible by 10

a = [5, 10, 15, 20, 25, 30]
value = []
new = []
for i in a:
    if i % 10 == 0 and i not in value:
        value.append(i)
    else:
        new.append(i)
print("Divisible by 10 : ",value)
print("Not Divisible by 10 : ", new)


#   (2) Replace elements greater than 20 with 0
#   (3) Find cumulative sum of the modified array
a = [5, 10, 15, 20, 25, 30]
total = 0
for i in range(len(a)):
    if a[i]>20:
        a[i] = 0
    total = total +a[i]
print("Modified array :", a)
print("Sum :" , total)


            
