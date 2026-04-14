import numpy as np

a = np.random.randint(1, 10, (3,3))

rot = np.rot90(a, -1)
print(rot)


a = np.random.randint(1,10,(3,3))
print(np.rot90(a))