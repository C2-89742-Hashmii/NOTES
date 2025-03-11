
# Write a Rectangle class in Python language, allowing you to build a rectangle 
# with length and width attributes. 
# Create a Perimeter() method to calculate the perimeter of the rectangle and a 
# Area() method to calculate the area of the rectangle.  
# Create a method display() that display the length, width, perimeter and area of 
# an object created using an instantiation on rectangle class. 
# Create a Parallelepiped child class inheriting from the Rectangle class and with 
# a  attribute and another Volume() method to calculate the volume of the 
# Parallelepiped. 

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    
    def Perimeter(self):
        return(f"The perimeter of Rectangle is : {(2*((self.length)+(self.width)))}")
        
    def Area(self):
        return(f"The Area of Rectangle is : {(self.length)*(self.width)}")
        
    def display(self):
        print(f"Length :-> {self.length} | Width :-> {self.width}  |  Perimeter :-> {self.Perimeter()} | Area :-> {self.Area()}")
        

class Parallelepiped(Rectangle):
    def __init__(self, length, width ,hight):
        super().__init__(length, width)
        self.hight=hight
        
    def volume (self):
        print (f"The volume of Rectangle is : {(self.length)*(self.width)*(self.hight)}")
    

rectangle1 = Rectangle(10,20)
rectangle1.display()



parallelepiped1=Parallelepiped(10,20,30)
parallelepiped1.volume()