# Q1: Find largest element

arr = [3,7,2,9,5]

max_val = arr[0]

for i in arr:
    if i > max_val:
        max_val = i

print(max_val)
