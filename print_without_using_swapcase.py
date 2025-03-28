# Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

# ask user for input
text = input("Input: ")

# initialize an empty string to store the result
swapped_text = "" 

# look through each character in the text
for char in text:
# check if the character is uppercase
    if char.isupper():
        swapped_text += char.lower()  # Convert to lowercase and store
    else:
        swapped_text += char.upper()  # Convert to uppercase and store

# print output
print(text)