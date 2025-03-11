
# Write a program to read 6 numbers and create a dictionary having keys EVEN 
# and ODD. 
# Dictionary's value should be stored in list. Your dictionary should be like: 
# {'EVEN':[8,10,64], 'ODD':[1,5,9]} 

num=[]
for i in range (1,7):
    input_num =int (input(f"Enter the {i} number : "))
    num.append(input_num)
    
print (f" The input list is : {num}")

odd_num=list(filter(lambda n: n%2!=0 , num))
even_num=list(filter(lambda n: n%2==0 , num))

res={
    "Odd":odd_num ,
    "Even":even_num}

print(res)
