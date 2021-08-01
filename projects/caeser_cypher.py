# caeser cypher project
# apply a cypher of 7 to the secret variable

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

choice = int(input("Would you like to, 1. make a cypher, 2. unlock a cypher, or 3. see an example: "))
example = "I hear the gooseberries are doing well this year, and so are the mangoes."
solution = ""
secret = None

if choice == 3:
    print(f"With the example text of.. \n {example} \n with a secret of 7, you get..")
    secret = 7
    for char in example.lower():
        if char == " ":
            solution += " "
        elif char in "!.?,":
            pass
#           Check for characters and skip over them so it doesn't get caught in .index()
        else:
           solution += alphabet[((alphabet.index(char) + secret) % len(alphabet))]
#           Adds the location of letter in the alphabet + the secret together to find new letter.
#           If it's greater than  the length of the alphabet, used modulo to find the wrap around location.

    print(solution)

elif choice == 1:
    new_text = input("Enter the sentence you would like to encrypt: ")
    secret = int(input("What number would you like the secret to be: "))

    for char in new_text.lower():
        if char == " ":
            solution += " "
        elif char in "!.?,":
            pass
        else:
           solution += alphabet[((alphabet.index(char) + secret) % len(alphabet))]

    print(solution)

elif choice == 2:
    new_text = input("Enter the cypher you want to decode: ")
    secret = int(input("What is the secret: "))

    for char in new_text.lower():
        if char == " ":
            solution += " "
        elif char in "!.?,":
            pass
        else:
           solution += alphabet[((alphabet.index(char) + secret) % len(alphabet))]

    print(solution)

else:
    print("Pick a number next time, bub.")