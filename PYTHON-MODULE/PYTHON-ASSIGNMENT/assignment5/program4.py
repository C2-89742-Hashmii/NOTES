
#  In following text count occurrence of each letter (irrespective of case).
# Hint: convert string to same case e.g. text.lower(). Do not use Counter collection. 
# text = """Python is a high-level, general-purpose programming language. Its 
# design philosophy emphasizes code readability with the use of significant 
# indentation. Python is dynamically typed and garbage-collected. It supports 
# multiple programming paradigms, including structured, object-oriented and 
# functional programming."""


test = """Python is a high-level, general-purpose programming language. Its 
 design philosophy emphasizes code readability with the use of significant 
 indentation. Python is dynamically typed and garbage-collected. It supports 
 multiple programming paradigms, including structured, object-oriented and 
 functional programming."""
 
text = test.lower()
res={}
for char in test:
    if char.isalpha():
        if char in res :
            res[char]+=1
        else :
            res[char]=1

print(res)
