import numpy as np

arr = np.random.randint(1,100,(6,6))
print(arr)
diff = np.sum(np.diag(arr)) - np.sum(np.diag(np.fliplr(arr)))
print(diff)