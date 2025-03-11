#Write a program to accept a 4 digit number and 
#a. Display face value of each decimal digit 
#b. Display place value of each decimal digit 
# c. Display no in reverse order by changing decimal place values If user 
# enters a 4 digit number 9361 output should be 
# a. 9 3 6 1 
# b. 9361 = 9 000 + 300 + 60 + 9 
# c. 1639 
##################################################################################################################
#For sec A
num=int(input("Enter the four digit number:"))
face_value=str(num)
# for digit in face_value:
#     print(digit , end="    ")
##################################################################################################################
#For sec B
first = (num // 1000) * 1000

second = (num // 100) % 10 * 100

third = (num // 10) % 10 * 10

fourth = num % 10
print((first//1000),(first//100),(first//10),(first) ,)

print(f"{num} = {first} + {second} + {third} + {fourth}")
##################################################################################################################
#For sec C
reverse=face_value[: : -1]
print(reverse)