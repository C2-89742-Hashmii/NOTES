# Write a program that will calculate the price for a quantity entered from the keyboard, given
# that the unit price is Rs 5 and there is a discount of 10 percent for quantities over 30 and a 15
# percent discount for quantities over 50.

quantity = int(input("Enter the quantity: "))
unit_price = 5
total_price = quantity * unit_price

if quantity > 50:
    total_price *= 0.85  
elif quantity > 30:
    total_price *= 0.90

print(f"The total price for {quantity} items is: Rs {total_price:.2f}")