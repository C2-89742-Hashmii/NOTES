# Write a Python program that calculates the sum of the squares of all odd 
# numbers in a list of integers using map() and filter() 


list1=[1,2,3,4,5,6,7,8,9]

odd_list=list(filter(lambda n:n%2!=0,list1))

Square_list=list(map(lambda n : n**2, odd_list))

print(f"The square of odd num in list is : {Square_list}")



