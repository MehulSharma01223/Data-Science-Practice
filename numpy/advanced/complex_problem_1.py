import numpy as np

a = np.random.randint(1, 10, (3,3))

mean = np.mean(a, axis=1, keepdims=True)
result = (a > mean).astype(int)

print(a)
print(result)


data = np.array([
    [25,50000,80],
    [30,60000,85]
])

mean = np.mean(data, axis=0)
std = np.std(data, axis=0)

z = (data - mean) / std
print(z)