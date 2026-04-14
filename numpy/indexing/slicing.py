import numpy as np

a = np.array([10, 20, 30, 40, 50])

print(a[1:4])
print(a[::-1])



a = np.array([10,20,30,40,50,60])
print(a[:3])
print(a[-2:])

# today question 
# 1.) First 3 elements extract karo
# 3.) Last 2 elements extract karo
# 4.) Index 2 ka element print karo
# 5.) Array reverse karo
# 6.) Slice (index 1 to 4) aur reverse karo
# 7.) Replace index 3 value with 999

# 1.)
a = np.arange(1,10)
print(a)
print(a[:3]) 

#  2.)
print(a[-2:])

#  3.)
print(np.where(a ==2)[0][0])

#  4.)
print(a[::-1])

#  5.)
c= a[1:4]
print(c[::-1])

#  6.)
d = np.arange(1,10)
d[3] == 999
print(d)