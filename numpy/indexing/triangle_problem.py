import numpy as np

a = np.random.randint(1, 50, (5,5))
row, col = np.indices((5,5))

a[row < col] = 0
a[row > col] = 1

print(a)


a = np.random.randint(1,100,(4,4))

upper = np.triu(a)
lower = np.tril(a)

print(upper)
print(lower)