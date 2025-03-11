
# . Write a function in python to count the number of lines from a text file 
# "story.txt" which is not starting with an alphabet "C". 
# Example: If the file "test.txt" contains the following lines: 
#        Connecting DB’s with Python. 
#         Working with DB’s using Python. 
#         Accessing and Manipulating DB’s. 
#         Creation of Python virtual Environment. 
#         Working with beautiful soup. 
#         Working with matplotlib, seaborn. 
# The function should display the output as 4 


def count():
    file1 = open(r"C:\Users\saiif\OneDrive\Desktop\Programming-concepts\Programming-concept\assignment8\story.txt", "rt")
    content=file1.read()
    lines = content.split('\n')
    res=len(lines)
    for item in lines:
        if item[0]=='C':
            res-=1
    return res
        
   
    
        
        
print(count())

