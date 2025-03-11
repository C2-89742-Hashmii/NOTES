#Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise.

list1=[1,3,4]
list2=[2,6,8,10,1]

def overlapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
            break
            
    else:
        return False


print (overlapping(list1,list2))