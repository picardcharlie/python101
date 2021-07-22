# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.

filename = "operators.pdf"
extension = ""
for char in filename:
    if char == ".":
        extension += char
    if extension == "." and char == "p":
        extension += char
    if extension == ".p" and char == "d":
        extension += char
    if extension == ".pd" and char == "f":
        extension += char
    if extension == ".pdf":
        print("It's a .pdf file!")

# Of course this only works for this file name and not how it should.

