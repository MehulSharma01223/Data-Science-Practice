import numpy as np
#  Q 1 .)
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print(np.dot(a, b))

#  Q 2.)
a = np.random.randint(1,10,(3,3))
b = np.random.randint(1,10,(3,3))

print(np.dot(a,b))

#  Q 3.)

ab = np.random.randint(1,10,(3,3))
ba = np.random.randint(1,10,(3,3))

print(" Multiplication  2 matrix",np.dot(ab,ba))

de= np.linalg.det(ab)
ds= np.linalg.det(ab)
print("1 matrix determine : ", de)
print("2 matrix determine : ", ds)

dsa = np.linalg.inv(ab)
dssa = np.linalg.inv(ba)


print("1 matrix inverse : ", de)
print("2 matrix inverse : ", ds)

#  Q 4.)

arr = np.random.randint(1,100,(4,4))
print("Original : ", arr)
count = arr.sum(axis = 1)
print("Row wise mean: ",count)
mean = arr.mean(axis= 0 )
print("Colummn wise mean : ",mean)

diag = np.diag(arr)
print("diagonal matrix : ",diag)

#  Q 5.)

arr1 = np.random.randint(1,50,(5,5))
n = arr1.shape[0]
row, col = np.indices((n,n))
result = np.where(row > col,1,
        np.where(col>row,0,arr1))
print("\nModified Array :\n",result)