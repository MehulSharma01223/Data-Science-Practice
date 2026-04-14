import numpy as np

a = np.arange(1, 11)
print("Array:", a)

print("Sum:", np.sum(a))
print("Mean:", np.mean(a))


A = np.array([1,2,3,4,5])
print(A**2)

#  Today Questions
# 1.) Largest element find karo (loop se)
# 2.) Smallest element find karo
# 3.) Sum without np.sum()
# 4.) Average manually
# 5.) Even numbers extract karo
# 6.) Count even numbers

#  1.)

arr = np.array([10, 45, 23, 67, 12])

largest = arr[0]

for i in arr:
    if i > largest:
        largest = i

print("Largest element:", largest) 

#  2.)

arr = np.array([10, 45, 23, 67, 12])

largest = arr[0]

for i in arr:
    if i < largest:
        largest = i

print("Smallest element:", largest)

# 3.)

arr = np.array([10, 45, 23, 67, 12])

largest = 0

for i in arr:
    largest+=i

print("sum:", largest)

# 4.)
arr = np.array([10, 45, 23, 67, 12])

largest = 0

for i in arr:
    largest+=i

print("sum:", largest)
print("Average", largest // len(arr))

# 5.)
arr = np.array([10, 45, 23, 67, 12])

largest = []

for i in arr:
    if i % 2 == 0:
        largest.append(int(i))
        

print(largest)

#  6.)

print("count even numbers",len(largest))
