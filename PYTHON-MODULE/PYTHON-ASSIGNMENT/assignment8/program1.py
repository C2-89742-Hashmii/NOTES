
#  Write a function in Python to count and display the total number of words in 
# a text file 



def count():
    file1 = open(r"C:\Users\saiif\OneDrive\Desktop\Programming-concepts\Programming-concept\assignment8\text1.txt", "rt")
    content=file1.read()
    res=content.split()
    return (f"The no. of words in the file is : {len(res)}")

print(count())




