import numpy as np

a = np.array([1,2,3,4,5])

result = np.where(a % 2 == 0, a**2, a**3)
print(result)



a = np.array([5,10,15,20,25])
a = np.where(a > 15, -1, a)
print(a)