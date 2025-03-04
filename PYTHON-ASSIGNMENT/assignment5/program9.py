
# rite a version of a palindrome recognizer that also accepts phrase 
# palindromes such as "Go hanga salami I'm a lasagna hog.",  
# "Was it a rat I saw?",  
# "Step on no pets",  
# "Sit on a potato pan, Otis",  
# "Lisa Bonet ate no basil",  
# "Satan, oscillate my metallic sonatas",  
# "I roamed under it as a tired nude Maori", 
# "Rise to vote sir", or the exclamation "Dammit, I'm mad!". 
# Note that punctuation, capitalization, and spacing are usually ignored. 

def palindrome(phrase):
    
    str= input
    res = ''.join([ char.lower() for char in str if char.isalnum()])
    pall_check = res[::-1]
    if res==pall_check:
        return True
    else:
        return False
    
input=input("Enter the phrase to check if it is palindrome or not : ") 
res= palindrome(input)
print(f"The given pharse is palindrome : {res}")


