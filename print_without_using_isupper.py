# Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

# ask the user for input
text = input("Input: ")

# define uppercase characters
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# check manually if all characters is on uppercase
for char in text:
    if char not in uppercase:   # if no, print False
        print("False")
        break
else:
    print("True")   # if yes, print True
    

        