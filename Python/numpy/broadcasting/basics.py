import numpy as np
#  Q 1.)

a = np.array([1, 2, 3])
print(a + 10)


# Q2. )
b = np.random.randint(1,10,(3,4))
print(b + 5)
print(b* 2)

#  Q 3.)

arr = np.array([1,2,3,4,5])

print(a + 10)

#  Q4 . )

arr1 = np.array([[1,2,3],
                [4,5,6]])

# Add [10,20,30] to each row
result = arr1 + np.array([10,20,30])
print(result)

#  Q 5.)


arr2 = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

# Row-wise add
row_add = np.array([10,20,30])

# Column-wise multiply
col_mul = np.array([[1],
                    [2],
                    [3]])

# Final result
result = (arr2 + row_add) * col_mul

print(result)

#  Q 6.)


arr3 = np.random.randint(1,50,(4,3))

# Step 1: row-wise mean 
row_mean = np.mean(arr3, axis=1, keepdims=True)

# Step 2: subtract karo
reult = arr3 - row_mean

print(arr3)
print(reult)

#  Q 7. )

arr4 = np.random.randint(1,100,(5,4))

# step 1:  column wise max

col_max = arr4.max( axis = 0)

#  column wise divide

new = (arr4 / col_max)

print(arr4)
print(new)


