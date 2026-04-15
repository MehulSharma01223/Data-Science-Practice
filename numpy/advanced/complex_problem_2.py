import numpy as np
# Q 1.)
a = np.random.randint(1, 50, (5,5))

rot = np.rot90(a, -1)
center = rot[1:4, 1:4]

print(center)
print("Sum:", np.sum(center))

#  Q 2. )
a = np.random.randint(1,100,(5,4))

norm = (a - np.min(a)) / (np.max(a) - np.min(a))
print(norm)


# Remove duplicates
arr = [1,2,2,3,4,4]
print(list(set(arr)))

# Common elements
A = [1,2,3,4,5]
B = [3,4,5,6]
print(set(A) & set(B))

# Matrix diagonal
a = np.random.randint(1,100,(4,4))
print(np.diag(a))



#  Q 3.)
a = np.random.randint(1,100,(5,5))

# Diagonal replace
np.fill_diagonal(a, 0)

# Anti-diagonal
a[np.arange(5), np.arange(4,-1,-1)] = 1

print(a)

# Q 4. )

arr = np.random.randint(1,100,(5,5))
 
print("Original Array : ", arr)


#  column-wise min & max
col_min = arr.min(axis=0)
col_max = arr.max(axis=0)

#  Min-Max scaling
normalized = (arr - col_min) / (col_max - col_min)

print("\nNormalized Array:\n", normalized)

# replace values > 0.8 with 999
result = np.where(normalized > 0.8, 999, normalized)

print("\nFinal Result:\n", result)

#  Q 5.)
a = np.array([[1,2],[3,4]])
print(a.T)

arr1 = np.random.randint(1,100,(6,6))
print("array",arr1)

c = arr1[1:5,1:5]
print(c)
top = c[0, :]
bottom = c[-1, :]
left = c[1:-1, 0]
right = c[1:-1, -1]

border_sum = top.sum() + bottom.sum() + left.sum() + right.sum()

print("\nBorder Sum:", border_sum)

#  Q 6.)


arr2 = np.random.randint(1, 50, (5, 5))
print("Original Array:\n", arr2)

# Step 1: row-wise mean
row_mean = arr2.mean(axis=1, keepdims=True)

# Step 2: condition apply (> row mean → 1 else 0)
binary = np.where(arr2 > row_mean, 1, 0)
print("\nBinary Matrix:\n", binary)

# Step 3: column-wise max index
col_max_idx = np.argmax(binary, axis=0)

# Step 4: set those positions = -1
binary[col_max_idx, np.arange(binary.shape[1])] = -1

print("\nFinal Result:\n", binary)
