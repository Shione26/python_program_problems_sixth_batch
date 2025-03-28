# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

# ask the user for inputs
text = str(input("Input: "))
# ask the user for the number of characters included the characters in the left and the space characters
width = int(input("Width: "))
# concatenate the text and the spaces minus the length of the text
result = text + " " * (width - len(text))
# print output
print(result)