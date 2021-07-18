# Fahrenheit to Celsius:
# ----------------------
# Write the necessary code to convert a degree in Fahrenheit
# to Celsius and print it to the console. Use variable names!

# F = (C * 1.8) + 32

fahrenheit = input("Enter Fahrenheit: ")
celcius = (int(fahrenheit) - 32) / 1.8
print("Celcius: " + str(celcius))