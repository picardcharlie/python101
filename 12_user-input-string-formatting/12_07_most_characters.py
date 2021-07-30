# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

first = input("Enter three strings: ")
second = input()
third = input()

if len(first) > len(second) and len(first) > len(third):
    print(f"{len(first)}, {first}")

elif len(second) > len(first) and len(second) > len(third):
    print(f"{len(second)}, {second}")

elif len(third) > len(first) and len(third) > len(second):
    print(f"{len(third)}, {third}")

else:
    print("There was no input or they are the same length.")