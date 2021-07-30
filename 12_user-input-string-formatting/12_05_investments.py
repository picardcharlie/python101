# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

print("Time to figure out how your investments are doing.")
amount = input("Enter your starting investment: ")
interest_rate = input("Enter your interest rate percentage: ")
years = input("Enter the amount of years you wish to invest: ")

if amount.isdigit() != True:
    new_amount = ""
    for char in amount:
        if char.isdigit() == True:
            new_amount += new_amount.join(char)
else:
    new_amount = amount

if interest_rate.isdigit() != True:
    new_interest = ""
    for char in interest_rate:
        if char.isdigit() == True:
            new_interest += new_interest.join(char)
else:
    new_interest = interest_rate

print(f"If you invest {new_amount} at {new_interest}% for {years} years, "
        f"you will have {((float(new_amount) * (float(new_interest) / 100)) * float(years)) + float(new_amount)} dollars.")
