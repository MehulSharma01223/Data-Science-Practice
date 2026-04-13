num = int(input("Enter a number: "))

for i in range(2, num + 1):
    if num % i == 0:
        print("Smallest divisor greater than 1 is:", i)
        break