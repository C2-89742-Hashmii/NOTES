
#  Create a class 'Student' with rollno, studentName, course, dictionary of 
# marks(subjectName -marks [5]). 
# Provide following functionalities 
# A. initializer 
# B. override __str__ method 
# C. accept student data 
# D. Print student data 
# E. accept records of 5 students and Print it 

class Student:
    def __init__ (self,rollno,studentName,course,marks):
        self.rollno = rollno
        self.studentName = studentName
        self.course = course
        self.marks = marks
        
    