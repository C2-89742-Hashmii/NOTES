
# Create a class named Mobile with attributes ModelName, Company, Price 
# and with methods: set_attributes, print_details and can_afford. 

class Mobile:
    def __init__(self, Modelname, Company, Price):
        self.Modelname = Modelname
        self.Company   = Company
        self.Price     = Price
        
    def print_details(self):
        print(f"Modelname : {self.Modelname}  , Company {self.Company} , Price {self.Price} ")
        
        
    def can_afford(self):
        if self.Price>=100000:
            print("Can not afford")
        else:
            print("Can easily afford")
            
mobile1=Mobile("Iphone","Apple",15000)
print(mobile1.Company)
print(mobile1.Modelname)
print(mobile1.Price)
mobile1.print_details()
mobile1.can_afford()

        
        