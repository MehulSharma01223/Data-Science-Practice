import numpy as np

a = np.random.randint(1, 10, (3,3))

mean = np.mean(a, axis=1, keepdims=True)
result = (a > mean).astype(int)

print(a)
print(result)