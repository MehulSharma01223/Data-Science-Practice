import numpy as np

a = np.random.randint(1, 50, (5,5))

rot = np.rot90(a, -1)
center = rot[1:4, 1:4]

print(center)
print("Sum:", np.sum(center))


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




a = np.random.randint(1,100,(5,5))

# Diagonal replace
np.fill_diagonal(a, 0)

# Anti-diagonal
a[np.arange(5), np.arange(4,-1,-1)] = 1

print(a)