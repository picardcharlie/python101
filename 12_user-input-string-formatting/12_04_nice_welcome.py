# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.

name = input("Enter your name: ")

if " " in name:
    split_name = name.split()
    final = split_name[0]
else:
    final = name

print(f"Welcome to the party {final}. HEY EVERYONE, {final.upper()} IS HERE!")