# write a function to return simple interest
# To calculate simple interest, you can use the formula: SI = (P × R × T) / 100. In this formula,
# • SI: Stands for simple interest
# • P: Represents the principal amount
# • R: Represents the interest rate per year
# • T: Represents the time in years



p=float(input("Enter the principal ammount:"))
r=float(input("Enter the rate of intrest per year:"))
t=float(input("Enter the time in years :"))

SI=(p*r*t)/100
print(f"Your simple intrest is {SI}")