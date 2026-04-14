import numpy as np

a = np.random.randint(1, 10, (3,3))

result = (a > 5).astype(int)
print(result)


a = np.array([1,1,2,2,3,3])
print(np.unique(a))