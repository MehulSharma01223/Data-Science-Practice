# import numpy as np

# a = np.random.randint(1,10,(3,3))
# # n = a.shape[0]
# # row,col = np.indices((n,n))

# # print(a)

# # roated = np.rot90(a,-1)
# # print(roated)
# # print(a.T[:,::-1])
# # a[row>col] = 1
# # a[col>row] = 0
# # print(a)
# print(a)

# b = np.mean(a,axis = 1,keepdims=True).astype(int)
# a[a>b] = 1
# a[a<b] = 0
# a[a==b] = 0 
# print(a)

import numpy as np

# Step 0: Create matrix
a = np.random.randint(1, 60, (4,5))
print("Original:\n", a)

# Step 1: Column mean
col_mean = np.mean(a, axis=0, keepdims=True)

# Step 2: Apply condition (+10 / -10)
a = np.where(a > col_mean, a + 10, a - 10)

print("\nAfter Condition:\n", a)

# Step 3: Row-wise max → 0
row_max_idx = np.argmax(a, axis=1)
a[np.arange(a.shape[0]), row_max_idx] = 0

print("\nFinal Output:\n", a)