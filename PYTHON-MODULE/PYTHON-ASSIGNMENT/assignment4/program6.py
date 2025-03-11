# Write a Python program that filters out all strings that have more than 5 
# characters from a list of strings using the filter() function. 
# Input: words = ['Red', 'Green', 'Yellow', 'Purple', 'Orange'] 
# Output: ['Yellow', 'Purple', 'Orange'] 

words = ['Red', 'Green', 'Yellow', 'Purple', 'Orange'] 

res=list (filter(lambda word : len(word)>5,words))

print (f"The resultent list is : {res}")

