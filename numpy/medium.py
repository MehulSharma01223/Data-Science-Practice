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

            

# =========================
# Day 3
# =========================


# Q7.  Create a (3×5) array
#      Reverse each row individually
#      Reverse each column individually

import numpy as np
a = np.random.randint(1,100,(3,5))

# reverse each row individually 
row_reverse = a[:,::-1] 

#      Reverse each column individually
col_reverse =  a[::-1,:]
print("Original: \n",a)
print("Row Reversed:\n", row_reverse)
print("Column Reversed:\n", col_reverse)


# Q8.  Create a (4×4) array

#      Extract upper triangle elements
#      Extract lower triangle elements
import numpy as np

# Create 4×4 array
a = np.random.randint(1, 100, (4, 4))

upper = []
lower = []

# Extract upper & lower triangle
for i in range(len(a)):
    for j in range(len(a[i])):
        
        # Upper triangle
        if j >= i:
            upper.append(a[i][j])
        
        # Lower triangle
        if i >= j:
            lower.append(a[i][j])

print("Array:\n", a)
print("Upper Triangle:", upper)
print("Lower Triangle:", lower)


# Q9  Create a (6×6) array
#     Extract all elements where row index == column index (diagonal)
#     Extract all elements where row index + column index = n-1 (anti-diagonal)
#     Find difference between their sums

import numpy as np

# Create 6×6 array
arr = np.random.randint(1, 100, (6, 6))
print("Array:\n", arr)

# Extract diagonal elements
diag = np.diag(arr)

# Extract anti-diagonal elements
anti = np.diag(np.fliplr(arr))

# Find difference between their sums
diff = np.sum(diag) - np.sum(anti)

print("Diagonal:", diag)
print("Anti-diagonal:", anti)
print("Difference:", diff)



# =========================
# Day 4
# =========================

# Q10.     Create a (3×4) array
#          Add 5 to all elements
#          Multiply entire array by 2
import numpy as np

arr = np.random.randint(1,10,(3,4))
arr = arr +5
print(arr)
arr = arr*2
print(arr)


#Q11.      Create a (4×4) array
#          Find sum of elements in each column
#          Find product of elements in each row
import numpy as np

a = np.random.randint(1, 100, (4, 4))
print("Array:\n", a)

# Sum of each column
total = a.sum(axis=0)

# Product of each row
prod = a.prod(axis=1)

print("Column Sum:", total)
print("Row Product:", prod)


# Q12.    Create two arrays of same size
#         Compare both arrays element-wise
#         Return True/False array

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([1, 0, 3, 5])

# Element-wise comparison
result = a == b

print("Array A:", a)
print("Array B:", b)
print("Comparison:", result)


# =========================
# Day 5
# =========================


# Q13.     Create a (5×3) array
#          Find index positions where value > 50

import numpy as np
a = np.random.randint(1,100,(5,3))
print(a)
index = np.where(a>50)
print(index)

# Q14.     Create array [2,4,6,8,10]
#          Create boolean mask for values > 5
#          Use mask to extract values

import numpy as np

ar = np.array([2,4,6,8,10])

mask = ar >5
print (mask)
print(ar[mask])


# Q15     Create array [10,20,30,40,50]
#         Shift elements right by 1 position

import numpy as np

A = np.array([10,20,30,40,50])

last = A[-1]
A[1:] = A[:-1]
A[0] = last
print(A)
