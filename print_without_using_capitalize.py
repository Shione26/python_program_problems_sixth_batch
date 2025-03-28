# Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

# ask the user for input
text = input("Input: ")
# convert the first string character to uppercase
first_letter = text[0].upper()
# convert the rest string to lowercase
rest_of_letters = text[1:].lower()
# concatenate
result = first_letter + rest_of_letters
# print output
print(result)