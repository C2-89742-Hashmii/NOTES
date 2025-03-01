# Write a program that prompts the user to input number of calls and calculate the monthly telephone bills
# as per the following rule:
# Minimum Rs. 200 for up to 100 calls.
# Plus Rs. 0.60 per call for next 50 calls.
# Plus Rs. 0.50 per call for next 50 calls.
# Plus Rs. 0.40 per call for any call beyond 200 calls.
call_num=int(input("Enter the number of calls :"))

if call_num<=100:
    print("your monthly bill is Rs 200 ")
elif 100<call_num<=150:
    extra=call_num-100
    bill=200+(extra*0.60)
    print(f"Your monthly  bill is Rs {bill} ")
elif 150<call_num<=200:
    extra=call_num-100
    bill=200+(extra*0.50)
    print(f"Your monthly  bill is Rs {bill} ")
else:
    extra=call_num-100
    bill=200+(extra*0.40)
    print(f"Your monthly  bill is Rs {bill} ")
    