# Make a trip cost calculator
# ask how many kilometers you are going
# the liters per kilometer usage of the car
# the price of a liter of fuel

print("Welcome to Trip Cost Analyzer 3.0")
print("Please fill out the form as accurately as possible.")

distance = float(input("How far are you traveling in kilometers: "))
car = float(input("How many kilometers does your car travel on one liter: "))
price = float(input("How much is a liter of fuel currently: "))

# (distance / car) * price = total cost

total = (distance / car) * price

print(f"The total cost for fuel for your trip will be {total:.2f} dollars") #Had to check how to change decimal places.