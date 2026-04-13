class Rectangle:
    def __init__(self,len,height):
        self.len=len
        self.height=height

    def area(self):
        sum = self.len *self.height
        print(sum)


class Circle:
    def __init__(self,radius):
        self.radius = radius
    def circumference(self):
        result = 2*3.14*self.radius
        print(result)
        
s1 = Rectangle(5,4)
s1.area()

s2 =Circle(4)
s2.circumference()


