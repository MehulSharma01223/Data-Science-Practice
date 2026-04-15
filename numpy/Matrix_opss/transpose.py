import numpy as np

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

a = np.random.randint(1,10,(3,3))
print(a.T)