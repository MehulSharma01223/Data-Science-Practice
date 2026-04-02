# Day 1

# Q1: Remove duplicates
arr = [1,2,2,3,4,4]
unique = []

for i in arr:
    if i not in unique:
        unique.append(i)

print(unique)

# Q2:  (1) Common elements
#      (2) Elements presents in A not in B

A = [1,2,3,4,5]
B = [3,4,5,6,7]
common = []
new = []
for i in  A:
    if i in B:
        if i not in common :
            common.append(i)
        else :
            new.append(i)
print("common:",common)
print("A not in B:",new)
            
