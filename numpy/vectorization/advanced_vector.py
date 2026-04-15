import numpy as np
#  Q 1. )
a = np.random.randint(1, 50, (4,5))

col_mean = np.mean(a, axis=0, keepdims=True)
a = np.where(a > col_mean, a + 10, a - 10)

print(a)

# Q 2.) 

ab = np.array([10,20,30,40,50])
ab[ab == 30] = 100
print(ab)

#  Q 3.)
arr = np.array([5,12,7,18,3,20])

result = np.where(arr > 10 , arr*arr,arr*arr*arr)
print(result)



#  Q 4. )
arr1 = np.random.randint(1,50,(4,4))
print("Original :\n ",arr1)
rsult = np.where(arr1 % 2 == 0 , arr1 / 2 , arr1 * 3)
print("Result : \n ",rsult)

#  Q 5. )

arr2 = np.random.randint(1,100,(5,5))
print("Qriginal : \n" , arr2)
rslt = np.where(arr2 > 70 ,1,
                np.where(arr2 <30,-1,0 ))
print("Result : \n" , rslt)