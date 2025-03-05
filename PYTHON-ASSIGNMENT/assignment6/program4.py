
# Write a Python program to create a Vehicle class with max_speed and 
# mileage instance attributes. 
# Write a python program to Create a child class Bus that will inherit all of the 
# variables and methods of the Vehicle class

class Vehicle:
    def __init__(self, max_speed , mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        
    def Print_info(self):
        print(f"max_speed : {self.max_speed} and mileage {self.mileage}  ")
        
        
class Bus(Vehicle):
    def __init__(self,max_speed,mileage):
        super().__init__(max_speed,mileage)
        
    def Print_info(self):
        super().Print_info()


bus1=Bus(120,"10km/l")
print(bus1.max_speed)
print(bus1.mileage)
bus1.Print_info()


    
    