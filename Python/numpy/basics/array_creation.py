import numpy as np

# Create array from list
a = np.array([1, 2, 3, 4, 5])
print(a)

# Create 2D array
b = np.array([[1, 2], [3, 4]])
print(b)

# Q1 Largest
arr = [3,7,2,9,5]
print(max(arr))

# Q2 Smallest
arr = [10,20,30,40,50]
print(min(arr))

# Q3 Sum & Average
A = [2,4,6,8,10]
total = sum(A)
avg = total / len(A)
print(total, avg)

# #  Today questions 
# 1.) Questions (DO THESE)
# 2.) List [1,2,3,4,5] ko NumPy array me convert karo
# 3.) 10 zeros ka array banao
# 4.) 5 ones ka array banao
# 5.) 1 se 20 tak numbers generate karo (arange)
# 6.) Even numbers 2–20 tak banao
# 7.) Random 5 numbers generate karo
# 8.) 3×3 matrix of random numbers

#  1.)
a = [1,2,3,4,5] 
b = np.array([1,2,3,4,5] )
print(a)
print(type(a))

# 2. )
b = np.zeros(10)
print(b)

#  3.) 
c = np.ones(5)
print(c)
#  4.)
d = np.arange(1,21)
print(d)

#  5.)
e = np.arange(2,21,2)
print(e)

#  6.)
f = np.random.randint(1,100,5)
print(f)


#  7.)

g = np.random.randint(1,100,(3,3))
print(g)