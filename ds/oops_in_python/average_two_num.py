class Student:
    def __init__(self,Name,Marks):
        self.Name =Name
        self.Marks = Marks

    def Avg(self):
        sum = 0
        for i in self.Marks:
            sum +=i
        print("",self.Name,"is your average score is : ",sum/3)

s1 = Student("Mehul Sharma" ,[88,87,48])
s1.Avg()