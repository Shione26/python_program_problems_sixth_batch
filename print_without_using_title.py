# Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

# ask user for input
text = input("Input: ")

# create an empty list to store the capitalized texts
capitalized = []

# split the strings
splitted_words = text.split()

# convert the first letter to uppercase and the rest to lowercase then store in the list
for word in splitted_words:
    first = word[0].upper()
    rest = word[1:].lower()
    capitalized.append(first + rest)

# join the splitted words back to one
result = " ".join(capitalized)
# print output
print(result)