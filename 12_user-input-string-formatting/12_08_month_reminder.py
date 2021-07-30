# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.

month = int(input("Enter a number between 1 and 12: "))

month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

if month > 12 or month < 1:
    print("Error")
else:
    print(f"That is {month_list[month]}")

#I really didn't want to make a huge nested if statement for all the months.  This is so much easier to read.