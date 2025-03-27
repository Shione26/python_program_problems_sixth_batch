# Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

# ask the user for input
text = input("Input: ")
# inspect each character if it is a non-space character
for char in text:
    if char == " ":          # if no, continue
        continue  
    if char != " ":          # if yes, break then print the rest of the characters
        break 
# print output
print(text)
