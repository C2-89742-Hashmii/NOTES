
#  Define a Circle class allowing to create a circleC (O, r) with center O(a, b) and 
# radius r using the constructor: 
# def init (self, a, b, r): 
# self.a = a 
# self.b = b 
# self.r = r 
# A:- Define a Area() method of the class which calculates the area of the circle. 
# B:- Define a Perimeter() method of the class which allows you to calculate the 
# perimeter of the circle. 


class Circle:
    def __init__(self,a,b,r):
        self.a = a
        self.b = b
        self.r = r
        
    def Area(self):
        print(f"The area of square is : {3.14*((self.r)*(self.r))}")
        
    def Perimeter(self):
        print(f"The perimeter of square is : {2*(3.14*(self.r))}")
        
        
circle1=Circle(2,3,4)
print(circle1.r)
circle1.Area()
circle1.Perimeter()
