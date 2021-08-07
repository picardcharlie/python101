# Use the modulo operator to confirm which of the values
# shown below are divisible by seven.

num_1 = 42
num_2 = 137
num_3 = 455
num_4 = 1997

print(num_1 % 7) #This one is
print(num_2 % 7) #Nope
print(num_3 % 7) #Yes
print(num_4 % 7) #No

numbers = [42,137,455,1997]
for number in numbers:
    if number % 7 == 0:
        print(number, " is divisible by 7.")

print(numbers[0])