import numpy as np

a = np.random.randint(1, 50, (4,5))

col_mean = np.mean(a, axis=0, keepdims=True)
a = np.where(a > col_mean, a + 10, a - 10)

print(a)


a = np.array([10,20,30,40,50])
a[a == 30] = 100
print(a)