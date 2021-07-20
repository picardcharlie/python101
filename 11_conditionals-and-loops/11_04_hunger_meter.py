# Your hunger-meter currently only handles string input accurately.
# Replace your first `if` statement with a type check.
# If the value of `hunger` is not of the type `str`,
# print a message that reminds you to
# declare your hunger levels with a string.


hunger = 2

if type(hunger) != str:
    print("Please use a string to answer")
elif hunger == "big":
    print("Eat the pizza")
elif hunger == "small":
    print("Eat the apple")
else:
    print("Don't eat anything")