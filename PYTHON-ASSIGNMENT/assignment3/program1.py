#Using for loop, write and run a Python program to find factorial from 0 to 10.#
def factorial(num):
    result=1
    for i in range (1,num+1,1):
        result*=i
    return result

number=int(input("Enter the number to find the factorial :"))
        
#fact_result= factorial(num)
print(f"The factorial of {number} is : {factorial(number)}")
        