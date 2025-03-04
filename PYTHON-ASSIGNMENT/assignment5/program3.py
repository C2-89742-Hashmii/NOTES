
#  Define a function subtract() that takes two lists and returns difference (i.e. 
# excess elements from list1). If list1 = [10, 20, 30, 40] and list2 = [30, 40, 50, 60], 
# then result should be [10, 20]. 

def subtract(l1,l2):
    s1=set(l1)
    s2=set(l2)
    return (s1-s2)


list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]



res=list(subtract(list1,list2))
print(res)