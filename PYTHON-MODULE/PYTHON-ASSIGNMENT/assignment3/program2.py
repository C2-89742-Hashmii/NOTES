#Write a program that accepts a list from user and print the alternate element of list.

########################################     METHOD 1      ##########################################
Length_of_list=int(input("Enter the number of element you want in list :"))
list=[]
for item in range(Length_of_list):
    data=(input(f"Enter the input of your list "))
    list.append(data)
    
print(list[::2])
    

