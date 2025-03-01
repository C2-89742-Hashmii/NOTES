#  Write a Python program that filters out numbers greater than 10 from a list 
# of numbers using the filter() function. 
# Input: numbers = [5, 12, 3, 18, 9, 20, 22, 21] 
# Output: [12, 18, 20, 22, 21] 

numbers = [5, 12, 3, 18, 9, 20, 22, 21] 

res=list(filter(lambda num : num>10 , numbers ))

print(f"The resltent lis is :{res}")