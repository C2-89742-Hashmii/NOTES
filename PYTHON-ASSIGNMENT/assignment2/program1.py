#Write A Program which is taking 5 int value and calculate sum of cube of all numbers [Write cube function]
num1=int(input("Enter the 1st number:"))
num2=int(input("Enter the 2nd number:"))
num3=int(input("Enter the 3rd number:"))
num4=int(input("Enter the 4th number:"))
num5=int(input("Enter the 5th number:"))

result=lambda num1,num2,num3,num4,num5 :(num1**3)+(num2**3)+(num3**3)+(num4**3)+(num5**3)

print(f"the sum of all numbers cube is : {result(num1,num2,num3,num4,num5)}")
for item in list:
    result+=item