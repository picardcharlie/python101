# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

string_input = input("Enter a string: ")
letter_input = input("Enter a letter: ")
location = 1

for char in string_input:
    if char == letter_input:
        print("Result:", location)
        break
    else:
        location += 1
    if location > len(string_input):
        print("The letter isn't inside")