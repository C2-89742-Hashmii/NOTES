#Write a function filter_long_words() that takes a list of words and an integer len and
# returns the list of words that are longer than len. 
########################################################################################################


list_input=input("Enter the word of list by comma seperated :")
list=list_input.split(",")   
length=int(input("Enter the length size :"))


def filter_long_words(list):
    new_list=[]
    for item in list:
        if len(item)>length:
            new_list.append(item)
    print(f"The updated list that are longer than len is :{new_list}")
    
print(f"Given list is :{list}")

filter_long_words(list)



        
    

