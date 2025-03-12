



class Staff :
    def __init__(self, id,name,type):
        self.__id=id
        self.__name=name
        self.__type=type
        
    
    
    def get_id (self):
        return self.__id
    
    def get_name (self):
        return self.__name
    
    def get_type (self):
        return self.__type
    
    def __str__(self):
        return f"id :{self.get_id()}\n name : {self.get_name}\n type : {self.__type}"
    
    
    
class Institute :
    def __init__(self , institute_name="Unknown Institute"):
        self.institute_name=institute_name
        self.staff_list=[]
    
    def __str__(self,staff):
        return f"institute name is :  {self.institute_name}\n  staff list is : {self.staff_list}"
    
    def add_staff(self,):
        for _ in range (5):
            self.staff_list.append(self.staff)
            
def institue():
    institue= Institute("Sunbeam")
    staff1 = Staff(101, "Alice", "teaching")
    staff2 = Staff(102, "Bob", "nonteaching")
    staff3 = Staff(103, "Charlie", "teaching")
    staff4 = Staff(104, "David", "nonteaching")
    staff5 = Staff(105, "Eve", "teaching")
    institue.append(staff1)
    institue.append(staff2)
    institue.append(staff3)
    institue.append(staff4)
    institue.append(staff5)
    
    
    
    
        