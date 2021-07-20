# Print the total number of vowels that are used in the lorem ipsum text.

lorem_ipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt 
mollit anim id est laborum."""

vowels = 0
for char in lorem_ipsum:
    if char == "a":
        vowels += 1
    elif char == "e":
        vowels += 1
    elif char == "i":
        vowels += 1
    elif char == "o":
        vowels += 1
    elif char == "u":
        vowels += 1

print(vowels)

#My first thought and it does work but...

count = 0
for char in lorem_ipsum:
    if char in "aeiou":
       count += 1

print(count)
#This is much shorter and easier to read.  I'm learning Mikey.