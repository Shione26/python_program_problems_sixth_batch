# Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

# ask the user for input
text = input("Input: ")
# ask the user for width
width = int(input("Width: "))
# subtract the length of the text to the width to get the number of spaces on both sides
total_spaces = width - len(text)
# divide the number of spaces into 2
left_spaces = total_spaces // 2
right_spaces = total_spaces - left_spaces
# concatenate the spaces with the text
result = " " * left_spaces + text + " " * right_spaces
# print output
print(result)