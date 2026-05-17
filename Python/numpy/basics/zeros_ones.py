import numpy as np

z = np.zeros((3,3))
o = np.ones((2,2))

print("Zeros:\n", z)
print("Ones:\n", o)

import numpy as np

A = np.array([5,10,15,20,25])
even = A[A % 2 == 0]
print(even)