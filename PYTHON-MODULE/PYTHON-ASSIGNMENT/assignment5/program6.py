
# Write a program in Python to find out the frequency of each number in 
# stored in a list using a python dictionary. 
# Example 
# List1 = [1,2,3,4,5,6,7,8,9,7,6,2,4,2,5,23,6,4] 
# Output ={1: 1, 2: 3, 3: 1, 4: 3, 5: 2, 6: 3, 7: 2, 8: 1, 9: 1, 23: 1}


List1 = [1,2,3,4,5,6,7,8,9,7,6,2,4,2,5,23,6,4]
output={}
for num in List1:
    if num in output:
        output[num]+=1
    else:
        output[num]=1
        
print(output)