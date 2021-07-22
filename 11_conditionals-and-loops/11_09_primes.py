# Print out every prime number between 1 and 1000.

for n in range(1000):
    if (n % 3 != 0) and (n % 2 != 0) and (n % 5 != 0) and (n % 7 != 0):
        print(n)

#so change one number?