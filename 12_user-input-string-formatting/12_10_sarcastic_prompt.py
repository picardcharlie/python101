# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

x = input("What is one of your strongest held opinions: ")
y = ""
for i in range(len(x)):
    if i % 2 == 0:
        y += x[i].capitalize()
    else:
        y += x[i]
print(y)