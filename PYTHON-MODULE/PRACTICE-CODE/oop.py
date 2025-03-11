
# class DOG :
#     def __init__(self, name,breed , OWNER):
#         self.name = name
#         self.breed = breed
#         self.OWNER =OWNER
#     def bark(self):
#         print("WHOOF WHOOF")
        
        
# class OWNER:
#     def __init__(self , name , mobile_number ,address):
#         self.name=name
#         self.mobile_number=mobile_number
#         self.address=address


# owner1 = OWNER("Saiif" ,"7985281683" , "Lucknow")
# dog1 = DOG("oreo" , "golden retriever", owner1 )
# dog1.bark()
# print (dog1.name)
# print (dog1.breed)
# print(owner1.name)

# print ("-"*50)

# owner2 = OWNER("Saiif" ,"7985281683" , "Lucknow")

# dog2 = DOG("builder" , "dogo argentino",owner2)
# dog2.bark()
# print (dog2.name)
# print (dog2.OWNER.mobile_number)
# print (owner2.address)


# ############################################################################################################################



# class Person :
#     def __init__ (self,name,age ):
#         self.name=name
#         self.age=age
        
#     def greet(self):
#         print(f"My name is {self.name} and my age is {self.age}")
        
        
# person1= Person("gdfgb",1521000)
# person1.greet()

# ############################################################################################################################



# Create a class 'Student' with rollno, studentName, course ,dictionary of 
# marks(subjectName -marks [5]). 
# Provide following functionalities 
# A. initializer 
# B. override __str__ method 
# C. accept student data 
# D. Print student data 
# E. accept records of 5 students and Print it 


class Student:
    def __init__(self, rollno , studentName,course,marks=None):
        self.__rollno=rollno
        self.__studentName=studentName
        self.__course=course
        self.__marks=marks if marks is not None else{}
        
    def __init__(self,marks=None):
        self.__marks=marks if marks is not None else{}
        
    def __str__(self):
        return f"rollno: {self.__rollno }\nstudentName : {self.__studentName}\ncourse : {self.__course}\nmarks :{self.__marks}"
    
    
    def accepter(self):
        rollno=int(input("Enter the roll number :"))
        self.__rollno=rollno
        studentname=(input("Enter the studentname :"))
        self.__studentName=studentname
        course=input("Enter the name of course : ")
        self.__course=course
        
        
        for _ in range(2):
            sub=input("Enter Subject name:")
            mark=int (input("Enter Subject marks:"))
            self.__marks[sub]=mark
            
            
student1=Student()
student1.accepter()
print(student1)


