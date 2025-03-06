
# Create a class product having (pid and manufacture_location) as private 
# f
#  ields,Create another class as Book having (name, 
# number_of_pages,author,price) as private fields. Specify _init(), getters, setters, 
# __str_() , print_data() Use correct OOP feature to implement this scenario. 
# a) display the details of the product and book 
# b) check if book price is 0 or negative then price is not valid otherwise print 
# valid price. 

class Product:
    def __init__(self,pid,manufacture_location):
        self.__pid= pid
        self.__manufacture_location= manufacture_location
        
        
    def get_pid (self):
        return self.__pid
    
    def get_manufacture_location (self):
        return self.__manufacture_location
    
    
    def __str__(self):
       return f"Product [ID : {self.__pid} , MANUFACTURE LOCATION : {self.__manufacture_location}"
    
    
    
    def display(self):
        print (f"The pid is : {self.get_pid()}")
        print (f"The manufacture_location is : {self.get_manufacture_location()}")
        
    
    
    
class Book:
    def __init__(self,name,number_of_pages,author,price):
        self.__name = name
        self.__number_of_pages = number_of_pages
        self.__author = author
        self.__price = price
        
    def get_name (self):
        return self.__name
        
    def get_number_of_pages (self):
        return self.__number_of_pages
    
    def get_author (self):
        return self.__author
    
    def get_price (self):
        return self.__price
    
    def __str__(self):
       return f"Book[Name: {self.__name}, Pages: {self.__number_of_pages}, Author: {self.__author}, Price: {self.__price}]"
    
    

    def display(self):
        print (f"The name of Book  is : {self.get_name()}")
        print (f"The number_of_pages in the book is : {self.get_number_of_pages()}")
        print (f"The author of Book  is : {self.get_author()}")
        print (f"The price of Book  is : {self.get_price()}")
        
        
    def validator(self):
        if self.get_price() > 0 :
            return "Price  for Book is  valid"
        else :
            return " Price for Book is not valid "
        
    
    
    
    
        
        
product1= Product (101 , "USA")



product1.display()


print ('-'*182)


book1= Book ("Ghost in the Wires" , 204 , "Kevin Metnick.." , 1900)

book1.display()

print (book1.validator())






































