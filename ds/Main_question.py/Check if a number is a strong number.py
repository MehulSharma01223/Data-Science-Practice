def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

num = int(input("Enter a number: "))
temp = num
sum_fact = 0

while temp > 0:
    digit = temp % 10
    sum_fact += fact(digit)
    temp //= 10

print("Strong Number" if sum_fact == num else "Not                                          a Strong Number")
