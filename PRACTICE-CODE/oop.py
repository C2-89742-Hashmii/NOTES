
class DOG :
    def __init__(self, name,breed , OWNER):
        self.name = name
        self.breed = breed
        self.owner =OWNER
    def bark(self):
        print("WHOOF WHOOF")
        
        
class OWNER:
    def __init__(self , name , mobile_number ,address):
        self.name=name
        self.mobile_number=mobile_number
        self.address=address


owner1 = OWNER("Saiif" ,"7985281683" , "Lucknow")
dog1 = DOG("oreo" , "golden retriever", owner1 )
dog1.bark()
print (dog1.owner.name)
print (dog1.breed)

print ("-"*50)

owner2 = OWNER("Saiif" ,"7985281683" , "Lucknow")

dog2 = DOG("builder" , "dogo argentino",OWNER)
dog2.bark()
print (dog2.name)
print (dog2.breed)
print (dog2.owner.name)

