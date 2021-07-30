# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

number = 0

while True:
    number = int(input("Enter a number between 1 and 1,000,000,000: "))

    if number <= 0 or number > 1000000000:
        print("Please enter a number within the range.")
        continue

    if number % 3 == 0:
        print("The number is divisible by 3")
        break

    else:
        print("The number is not divisible by 3.")
        break