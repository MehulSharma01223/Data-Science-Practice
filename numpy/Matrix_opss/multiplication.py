import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print(np.dot(a, b))


a = np.random.randint(1,10,(3,3))
b = np.random.randint(1,10,(3,3))

print(np.dot(a,b))