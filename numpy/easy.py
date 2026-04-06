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
