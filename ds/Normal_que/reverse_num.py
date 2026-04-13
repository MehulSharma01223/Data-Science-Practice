# a = int(input("Enter a num : "))
# for i in range (a,0,-1):
#     print(i)
# a = [5,10,15,20,25,30]
# sum = []
# for i in a:
#     if i > 20:
#         p = a.index(i)
#         a[p] = 0
# sum += int(i) 
# print(a)
# print(sum)
import numpy as np

# Create a array

import numpy as np
A = np.array([10,20,30,40,50])

#      Replace values > 30 with -1
A[A > 30] = -1

#      Find cumulative sum after replacement
total = 0
cumulative = []

for i in A:
    total+=i
    cumulative.append(total)

np_cumsum = np.cumsum(A)
print(A)
print(cumulative)
print(np_cumsum)