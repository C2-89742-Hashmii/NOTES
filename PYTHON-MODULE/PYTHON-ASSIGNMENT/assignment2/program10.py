# write a function to return compound interest.
# CI = P (1 + r/n) ^ nt
# P - Principal Amount
# r - Rate of interest
# n - Number of times interest compounds in a year
# t - Number of years

p=int(input("Enter the principal ammount:"))
r=int(input("Enter the rate of intrest :"))
n=int(input("Enter the Number of times interest compounds in a year :"))
t=int(input("Enter Number of years :"))


def Compound_intrest(p,r,n,t):
    CI= (p * (1 +(r/n)) ** (n * t))-p
    return CI
result=Compound_intrest(p,r,n,t)

print (f"the compund intrest is {result} ")