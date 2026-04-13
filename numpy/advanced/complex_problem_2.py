import numpy as np

a = np.random.randint(1, 50, (5,5))

rot = np.rot90(a, -1)
center = rot[1:4, 1:4]

print(center)
print("Sum:", np.sum(center))