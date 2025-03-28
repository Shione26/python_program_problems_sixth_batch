# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

# ask the user for input 
# ask the user for the number of characters included the characters in the left and the space characters
# 

text = input("Input: ")
width = input("Width: ")
space = " "

output = text + (space * width - (len(text)))

print(output)