# Write a Python program that finds the longest word in a list of strings. Use 
# map() to calculate the length of each word, and filter() to get the word with the 
# maximum length. 

#####################################################################################################################################


list_Words = ["python", "functional", "programming", "is", "powerful"]

length_of_world=list(map(lambda n : len(n),list_Words))

print(length_of_world)

m=max(length_of_world) # it find the max and store in 'm' variable 
print(m)
Max_length_word=list(filter(lambda  n:len(n)==m ,list_Words))
print(Max_length_word)





