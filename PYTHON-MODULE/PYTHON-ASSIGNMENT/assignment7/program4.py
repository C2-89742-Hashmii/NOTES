
# Write a Class Painting with method calculatePaintingCost. Write a Class 
# FlatPainting with noOfRooms which is inheritated from Class Painting. Override 
# calculatePaintingCost. (Assume per room painting cost is 10000). 
# Write a Class BulidingPainting with noOfFlats which is inheritated from Class 
# Painting. Override calculatePaintingCost. (Assume per Flats painting cost is 
# 25000) Write method for 1.Flat 2.Building and then calculate the cost according 
# to the type. 

class Painting :
    def __init__(self,noOfRooms):
        self.noOfRooms= noOfRooms
        
    def calculatePaintingCost(self):
        return f"The calculatePaintingCost is {1000*self.noOfRooms}"
    
    
        
    
class FlatPainting(Painting):
    def __init__(self, noOfRooms):
        Painting.__init__(self,noOfRooms)
        
    def calculatePaintingCost(self):
        return f"The calculatePaintingCost is {1000*self.noOfRooms}"
    
class BulidingPainting(Painting):
    def __init__(self,noOfRooms):
        Painting.__init__(self,noOfRooms)
        
        
        
    def calculatePaintingCost(self):
        return f"The updated calculatePaintingCost is {25000*self.noOfRooms}"
    
    
    
flatPainting1 = FlatPainting(10)

print(flatPainting1.calculatePaintingCost())


bulidingPainting1 =BulidingPainting (10)   
print(bulidingPainting1.calculatePaintingCost())
        
        
        