# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

string = input("Enter a sentence: ")

a, e, i, o, u = 0, 0, 0, 0, 0

for char in string:
    if char == "a":
        a += 1
    if char == "e":
        e += 1
    if char == "i":
        i += 1
    if char == "o":
        o += 1
    if char == "u":
        u += 1

print(f"Your sentence had {a} A's, {e} E's, {i} I's, {o} O's and {u} U's in it.")