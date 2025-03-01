# Write a Python program that adds two lists element-wise using the map() 
# function. 


list1 = [1, 2, 3, 4, 5] 

list2 = [5, 4, 3, 2, 1] 

res_list=list(map(lambda l1 , l2 : l1+l2 , list1,list2))

print(f"The resultent list is : {res_list}")
