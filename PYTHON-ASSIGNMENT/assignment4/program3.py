# Write a Python program to convert a given list of integers and a tuple of integers into a list of strings. Use Python map. 

#####################################################################################################################################


list1 = [1,2,3,4,5,6,7,8,9] 

tup1=1,2,3,4,5,6,7,8,9

res1=list(map(lambda n : str(n),list1))

res2=tuple(map(lambda n : str(n),tup1))

print(res1)

print(res2)

