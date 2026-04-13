class Calculator:
    def __init__(self,num1 ,num2):
        self.num1 =num1
        self.num2 =num2

    def add(self):
        result = self.num1 +self.num2
        print(result)

    def sub(self):
        result = self.num1 - self.num2
        print(result)

    def multiply(self):
        result = self.num1*self.num2
        print(result)

    @staticmethod
    def say():
        print("Hello Bro & Sister ")
        
    def division(self):
        if self.num2 != 0:    
            result = self.num1 / self.num2
            print(result)
        else:
            print("Can't divide by zero")

s1 = Calculator(5,6)
s1.say()
s1.add()
s1.sub()    
s1.multiply()
s1.division()
