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

# =========================
# Day 2
# =========================

# Q4: Find common elements
#     Find uncommon elements (both sides)

# Ans
A = [1,2,3,4,5]
B = [4,5,6,7,8]
common = []
uncommon = []

# common elements
for i in A:
    if i in B:
        common.append(i)

# A me jo B me nahi
for i in A:
    if i not in B:
        uncommon.append(i)

# B me jo A me nahi
for i in B:
    if i not in A:
        uncommon.append(i)
print("Common value :",common)
print("Not common value : ",uncommon)

# Q5: Create a (4×4) array
#     Extract diagonal elements
#     Find sum of diagonal

# Ans
import numpy as np

# Create a array
a = np.random.randint(1,100,(4,4))

# Extract diagonal elements
b = []
total = 0 
for i in range(len(a)):
    b.append(int(a[i][i]))

#     Find sum of diagonal

for i in b:
    total+=[i]
print("there are diagonal value : ",b)
print("all the diagonal value total : ",total)


# Q6.  Given:
#      A = [10,20,30,40,50]
#      Replace values > 30 with -1
#      Find cumulative sum after replacement

import numpy as np
A = np.array([10,20,30,40,50])

#      Replace values > 30 with -1
A[A > 30] = -1

#      Find cumulative sum after replacement
total = 0
cumulative = []

for i in A:
    total+=i
    cumulative.append(int(total))

print(A)
print(cumulative)

            
