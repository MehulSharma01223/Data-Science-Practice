import numpy as np

# Q1
arr1 = np.array([5, 15, 25, 35, 45])
print(arr1[arr1 > 20])

# Q2
arr2 = np.array([5,12,7,18,3,20])
print(arr2[arr2 > 10])

# Q3 (Main Question)
arr = np.array([5, 12, 7, 18, 3, 20, 25, 30])

print("Original:", arr)

mask = (arr > 10) & (arr < 25)

extracted = arr[mask]
count = np.sum(mask)

arr[mask] = -1

print("Extracted:", extracted)
print("Updated:", arr)
print("Count:", count)

#  Q3. )

arr3 = np.array([10,25,30,45,50,65])

print("Original : ",arr3)

msk = (arr3 > 20) & (arr3 <60)

new = arr3[msk]

co = np.sum(msk)
arr3[msk] = -1


print("Extracted:", new)
print("Updated:", arr3)
print("Count:", co)
