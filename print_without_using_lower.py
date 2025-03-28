# Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

# ask the user for input
text = input("Input: ")

# create a list of uppercase letters
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# create a list of lowercase letters
lowercase = "abcdefghijklmnopqrstuvwxyz"

# initialize an empty string to store the output
result = ""

# check if character is in the list of uppercase
for char in text:
    if char in uppercase:
        index = uppercase.index(char)      # if yes, find the position of that uppercase 
        result += lowercase[index]        # convert it to its corresponding index in lowercase then store in the initialized empty string
    else:
        result += char                    # if no, just store the lowercase letter in the empty string
   
# print output
print(result)
