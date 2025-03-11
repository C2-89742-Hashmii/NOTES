
# 1) Given a dictionary of students and their favourite colours: 
# people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'} 
# A. Find out how many students are in the list 
# B. Change Lisa’s favourite colour 
# C. Remove 'Jenny' and her favourite colour 
# D. Sort and print students and their favourite colours alphabetically by name 




people={
    'Arham':'Blue',
    'Lisa': 'Yellow',
    'Vinod':'purple',
    'Jenny':'Pink'
}


print (f"The no. of student in collection are : {len(people)}")

people['Lisa']='black'

print(people)

people.pop('Jenny','pink')

print(people)



