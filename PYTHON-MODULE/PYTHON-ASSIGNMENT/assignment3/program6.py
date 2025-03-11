#Find and display the largest number of a list without using built-in function max(). 
#Your program should ask the user to input values in list from keyboard.
list = []
print(" 'REMINDER' ->  Type 'Y' when you are done putting all number in list")
flag = True
while flag==True:
    a = input("Enter Value for the list : ")
    if a == "Y" or a=='y':
        flag = False
    else:
        list.append(a)
        
print(list)
max_val=list[0]

for item in list:
    if item>max_val:
        max_val=item

print(f"The largest number  in the list is : {max_val} ")