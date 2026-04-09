# Q1: Find largest element

arr = [3,7,2,9,5]

max_val = arr[0]

for i in arr:
    if i > max_val:
        max_val = i

print(max_val)

# Q2: Find smallest element

arr = [10, 20, 30, 40, 50]

min_val = arr[0]

for i in arr:
    if i <min_val:
        min_val = i
print(min_val)


# =========================
# Day 2
# =========================

# Q3: Create a NumPy array [2,4,6,8,10]

#    Find the sum without using np.sum()
#    Find the average manually

#  Ans 
A = [2,4,6,8,10]
#   Find the sum without using np.sum()
total = 0 
for i in A:
    total += i
print(total)

#    Find the average manually

avg = total / len(a)

print(avg )


# Q4:  Create array [5,10,15,20,25]
#     Find all even numbers
#     Count how many even numbers are present
# Ans

import numpy as np

A = np.array([5,10,15,20,25])

# Even numbers
even = A[A % 2 == 0]

# Count
count = len(even)

print(even)
print(count)




# =========================
# Day 3
# =========================

#    Q 5. Create array [2, 5, 8, 11, 14]
#         Find difference between consecutive elements
#         (Output: [3,3,3,3])

A = np.array([2, 5, 8, 11, 14])
diff = np.diff(A)
print(diff)


#  Q6.    Create array [10,20,30,40,50]
#         Swap first and last element
#         Swap second and second-last element

import numpy as np
a = np.array([10,20,30,40,50])
n = len(a)
for i in range(n//2):
    temp = a[i] 
    a[i] = a[n-i-1]
    a[n-i-1] = temp

print(a)
    

#  Q7.   Create array [1,2,3,4,5]
#        Create a new array where
#        each element = square of previous array

import numpy as np
A = np.array([1,2,3,4,5])

new = A **2
print(new)



# =========================
# Day 4
# =========================

#  Q7.   Create array [3,6,9,12,15]
#        Find difference between first and last element
#        Find middle element



import numpy as np

A = np.array([3,6,9,12,15])

# Difference
b = A[-1] - A[0]

# Middle element
middle = A[len(A)//2]

print("Difference:", b)
print("Middle element:", middle)


# Q8.   Create array [2,4,6,8]
#       Insert value 10 at the end
#       Insert value 0 at the beginning
import numpy as np
a = np.array([2,4,6,8])
a[0] = 0
a[len(a)-1] = 10
print(a)


# Q9.   Create array [1,2,3,4,5]
#       Remove element 3
#       Print updated array

import numpy as np

a = np.array([2,4,6,8])

# Insert 10 at end
a = np.insert(a, len(a), 10)

# Insert 0 at beginning
a = np.insert(a, 0, 0)

print(a)

# =========================
# Day 5
# =========================

# Q10.   Create array [10,20,30,40]
#        Convert array into list
#        फिर list को वापस array में convert करो


import numpy as np
a = np.array([1,2,3,4,5])
pritn(type(a))
b = list(a)
print(type(b))
b = np.array(a)
print(type(b))



# Q11.   Create array [5,10,15,20,25]
#        Find index of value 15
#        Replace that value with 100
import numpy as np

a = np.array([5,10,15,20,25])

a[a ==15] = 100
print(a)


# Q12.    Create array [1,1,2,2,3,3]
#         Remove duplicate elements
#         Print unique array


import numpy as np

a = np.array([1,1,2,2,3,3])

unique = []

for i in a:
    if i not in unique:
        unique.append(i)

# convert back to numpy array
unique = np.array(unique)

print("Unique array:", unique)

# =========================
# Day 6
# =========================


# Q.    Create array [10,20,30,40,50,60]
#       Extract first 3 elements
#       Extract last 2 elements

import numpy as np

# Create array
arr = np.array([10, 20, 30, 40, 50, 60])

# Extract first 3 elements
first_three = arr[:3]

# Extract last 2 elements
last_two = arr[-2:]

print("Original Array:", arr)
print("First 3 elements:", first_three)
print("Last 2 elements:", last_two)


# Q.       Create array [5,12,7,18,3,20]
#          Extract elements greater than 10
#          Count how many elements > 10

import numpy as np

a = np.array([5,12,7,18,3,20])

# Extract elements > 10
b = a[a > 10]
# Count elements > 10
count = b.size   # ya len(b)
print("Elements > 10:", b)
print("Count:", count)


# Q.     Create array [100,200,300,400,500]
#        Print element at index 2
#        Replace element at index 3 with 999

import numpy as np

a = np.array([100,200,300,400,500])

# Print element at index 2
print(a[2])

# Replace element at index 3 with 999
a[3] = 999

print(a)



# =========================
# Day 7
# =========================


# Q.     Create array [10,20,30,40,50,60]
#        Extract elements from index 1 to 4
#        Reverse that sliced part

import numpy as np

# Create array
a = np.array([10,20,30,40,50,60])

# Extract elements from index 1 to 4
sliced = a[1:5]

# Reverse that sliced part

reversed_part = sliced[::-1]

print("Original Array:", a)
print("Sliced Part:", sliced)
print("Reversed Part:", reversed_part)

# Q.     Create array [5,12,7,18,3,20]
#        Extract values divisible by 3
#        Replace those values with 0

import numpy as np

a = np.array([5,12,7,18,3,20])

# Extract values divisible by 3
b = a[a % 3 == 0]

# Replace those values with 0
a[a % 3 == 0] = 0

print("Divisible by 3:", b)
print("Updated array:", a)

#  Q.     Create array [100,200,300,400,500]
#         Swap elements at index 1 and index 3

import numpy as np

a = np.array([100,200,300,400,500])

last = a[3]
a[3] = a[1]
a[1] = last

print(a)



# =========================
# Day 8
# =========================

#  Q.     Create array [10,20,30,40,50]
# Extract elements from index 1 to 3
# Reverse that extracted part

import numpy as np

a = np.array([10,20,30,40,50])

# Extract index 1 to 3
part = a[1:4]

# Reverse that part
reversed_part = part[::-1]

print("Extracted:", part)
print("Reversed:", reversed_part)
