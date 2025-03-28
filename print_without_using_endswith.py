# Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

# ask the user for input
text = input("Input: ")
# ask the user the suffix
suffix = input("Suffix: ")

# check if the suffix is at the end of the index
if text[-len(suffix):] == suffix:
    print("True")   # if yes, print True
else:
    print("False")  # if no, print False
