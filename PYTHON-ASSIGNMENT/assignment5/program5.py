
# In cryptography, a Caesar cipher is a very simple encryption techniques in 
# which each letter in the plain text is replaced by a letter some fixed number of 
# positions down the alphabet. For example, with a shift of 3, A would be 
# replaced by D, B would become E, and so on. The method is named after Julius 
# Caesar, who used it to communicate with his generals. ROT-13 ("rotate by 13 
# places") is a widely used example of a Caesar cipher where the shift is 13. In 
# Python, the key for ROT-13 may be represented by means of the following 
# dictionary: 
# key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 
# 'l':'y', 'm':'z', 'n':'a', 
# 'o':'b','p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 
# 'A':'N', 'B':'O', 'C':'P', 
# 'D':'Q', 'E':'R','F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A','O':'B', 
# 'P':'C', 
# 'Q':'D','R':'E', 'S':'F', 'T':'G','U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'} 
# Your task in this exercise is to implement an encoder/decoder of ROT-13. Once 
# you're done, You will be able to read the following secret message: 
# Pnrfne pvcure? V zhpu cersre Pnrfne fnynq! 
# Note that since English has 26 characters, your ROT-13 program will be able to 
# both encode 
# And decode texts written in English. 



key=  {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 
'l':'y', 'm':'z', 'n':'a', 
'o':'b','p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 
'A':'N', 'B':'O', 'C':'P', 
'D':'Q', 'E':'R','F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A','O':'B', 
'P':'C', 
'Q':'D','R':'E', 'S':'F', 'T':'G','U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'} 

coded_msg="Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"

def decoder (msg,key):
    decoded_msg=""
    for char in msg :
        if char in key :
            decoded_msg += key[char]
        else:
            decoded_msg+=char
            
    return decoded_msg

res=decoder(coded_msg,key)

print(f"Result after decoing is :-> {res}")
            