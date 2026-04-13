num = int(input("Enter a num :-"))
for i in range(1,num):
    temp=num
    power = len(str(num))
    sum = 0 
while num>0:
    digit = num%10
    sum = sum + digit**power
    num =  num//10


if sum == temp:
    print("this num is Armstrong num")
else :
    print("This num not a Armstrong num")