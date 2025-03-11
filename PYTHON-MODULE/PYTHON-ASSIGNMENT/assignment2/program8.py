# Write a program that prompts the user to input a character and determine the character is
# vowel or consonant.
char = input("Enter a Single character : ")
if char in 'aeiou' :
    print(f"{char} is a vowel.")
elif char in 'AEIOU' :
    print(f"{char} is a vowel.")
else:
    print(f"{char} is a consonant")

