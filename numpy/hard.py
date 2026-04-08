# Q 1 : Standardize dataset using Z-score normalization

import numpy as np

# Create dataset (rows = samples, columns = features)
import numpy as np

data = np.array([
    [25, 50000, 80],
    [30, 60000, 85],
    [35, 65000, 90],
    [40, 70000, 95],
    [45, 80000, 100],
    [28, 52000, 82],
    [32, 58000, 88],
    [38, 72000, 92],
    [42, 75000, 96],
    [50, 90000, 105]
])
# Step 1: Calculate mean of each column
mean = np.mean(data, axis=0)

# Step 2: Calculate standard deviation
std = np.std(data, axis=0)

# Step 3: Apply Z-score formula
z_score = (data - mean) / std

#Step 4: Outlier Detection
outliers = data[np.abs(z_score) > 2]

print("Standardized Data:\n", z_score)
print("There are output of outliers " ,outlier)


# Q2.
#     (1)Find row-wise maximum values
#     (2)Find column-wise minimum values
#     (3)Normalize the entire array using Min-Max scaling (0 to 1)
#     (4)Identify values greater than 0.8 after normalization
import numpy as np
a = np.random.randint(1,100,(5,4))

#     (1)Find row-wise maximum values
Max = np.max (a,axis = 1)

#     (2)Find column-wise minimum values
Min = np.min(a, axis = 0)

#     (3)Normalize the entire array using Min-Max scaling (0 to 1)

Max_num = np.max(a)
Min_num = np.min(a)

# Normalized 
Normalized = ((a - Min_num) / (Max_num - Min_num))

Value = Normalized [Normalized>0.8]
print(a)

print("Maximum Value row wise : ", Max )
print("Minimum Value coloumn wise : ",Min ) 
print("Normalized: ",Normalized)
print("statisfy the condition : " , Value)


# =========================
# Day 2
# =========================

# Q3: Create a (5×5) array
        #Replace all even numbers with 0
        #Replace all odd numbers with 1
        #Count number of 0s and 1s
import numpy as np
a = np.random.randint(1,100,(5,5))
a[ a%2 == 0] = 0
a[ a%2 != 0] = 1 
num1 = np.sum(a==0])
num2 = np.sum(a==1)
print(a)
print("count 0 : ", num1)
print("count 1 : ", num2)


# Q4:Create two (3×3) matrices

#   Perform matrix multiplication
#   Find transpose of result
#   Extract diagonal of result
import numpy as np
a = np.random.randint(1,100,(3,3))
b = np.random.randint(1,100,(3,3))
c = np.dot(a,b)
t = c.T
d = np.diag(c)

print("Matrix A:\n", a)
print("Matrix B:\n", b)
print("Multiplication Result:\n", c)
print("Transpose:\n", t)
print("Diagonal:", d)

# Q5. Create a (6×4) NumPy array with random integers (1–100)
# (1) Find row-wise mean
# (2) Find column-wise standard deviation
# (3) Normalize each column (Min-Max scaling using axis=0)
# (4) Find all values less than 0.2 after normalization
# (5) Replace those values with -1
import numpy as np

a = np.random.randint(1, 100, (6,4))

# Row-wise mean
row_mean = np.mean(a, axis=1)

# Column-wise std
col_std = np.std(a, axis=0)

# Normalization
Normalized = (a - np.min(a, axis=0)) / (np.max(a, axis=0) - np.min(a, axis=0))

# Store values to be replaced
low_values = Normalized[Normalized < 0.2]

# Replace
Normalized[Normalized < 0.2] = -1

print("Array:\n", a)
print("Row mean:", row_mean)
print("Column std:", col_std)
print("Values replaced (<0.2):", low_values)
print("Final Normalized array:\n", Normalized)


# =========================
# Day 3
# =========================


# Q6 .Create a (5×5) array  
#     Replace diagonal elements with 0 Replace 
#     anti-diagonal elements with 1 Keep rest same

import numpy as np

# Create 5×5 array
a = np.random.randint(1, 100, (5, 5))
print("Original Array:\n", a)

n = len(a)

# Replace diagonal with 0
np.fill_diagonal(a, 0)

# Replace anti-diagonal with 1
a[np.arange(n), np.arange(n-1, -1, -1)] = 1

print("\nModified Array:\n", a)

# Q7. Create a (6×6) array
#     Extract all elements where row index == column index (diagonal)
#     Extract all elements where row index + column index = n-1 (anti-diagonal)
#     Find difference between their sums

import numpy as np

# Create 6×6 array
a = np.random.randint(1, 100, (6, 6))
print("Array:\n", a)

# Diagonal elements
diag = np.diag(a)

# Anti-diagonal elements
anti = np.diag(np.fliplr(a))

# Difference between sums
diff = np.sum(diag) - np.sum(anti)

print("\nDiagonal:", diag)
print("Anti-diagonal:", anti)
print("Difference:", diff)


# =========================
# Day 5
# =========================

# Q.     Create a (5×5) array
#        Find row index and column index of maximum element

import numpy as np

a = np.random.randint(1, 100, (5,5))
print(a)

# index of max element
index = np.unravel_index(np.argmax(a), a.shape)

print("Max value:", np.max(a))
print("Row index:", index[0])
print("Column index:", index[1])

# Q.    Create a (4×4) array
#       Replace border elements with -1
#       Keep inner elements same
import numpy as np

a = np.random.randint(1, 100, (4,4))
print("Original:\n", a)

# Replace borders
a[0, :] = -1      # top row
a[-1, :] = -1     # bottom row
a[:, 0] = -1      # left column
a[:, -1] = -1     # right column

print("\nModified:\n", a)


# Q.     Create a (6×6) array
#        Extract elements where row index is even 
#        Extract elements where column index is odd

import numpy as np

a = np.random.randint(1, 100, (6,6))
print("Array:\n", a)

# Row index even
even_rows = a[::2, :]

# Column index odd
odd_cols = a[:, 1::2]

print("\nEven Rows:\n", even_rows)
print("\nOdd Columns:\n", odd_cols)



# =========================
# Day 7
# =========================


#  Q.     Create a (6×6) array
#         Extract elements where:
#         value > 20 AND value < 80 AND divisible by 5
#         Replace them with negative

import numpy as np

a = np.random.randint(1,100,(6,6))

mask = (a > 20) & (a < 80) & (a % 5 == 0)

a[mask] = -a[mask]

print(a)
