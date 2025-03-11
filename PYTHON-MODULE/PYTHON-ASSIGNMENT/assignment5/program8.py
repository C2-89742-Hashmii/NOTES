
# Write a function translate() that will translate a text into "rövarspråket" 
# (Swedish for "robber's language"). That is, double every consonant and place 
# an 
# occurrence of "o" in between. For example, translate("this is fun") should 
# return 
# the string "tothohisos isos fofunon"

def translate(string):
    vowels="aeiouAEIOU"
    res=""
    for char in string:
        if char.isalpha() and char not in vowels:
            res+=char + "o"+ char
        else:
            res+= char
            
    return res
            
input=input("Enter the string to convert them in rövarspråket : ")
print(input)

print(f"After converting the input the resulten string is : {translate(input)}")
    
    