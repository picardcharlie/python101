# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.
# guess a number between 1 - 10 and get three tries.

import random

lives = 3
number = random.randint(1,10)
print(f"Guess a number between 1 and 10, you have {lives} lives to guess it!")

while lives > 0:
    guess = int(input("What is your guess: "))

    if guess == number:
        print("You got it! Nice work!")
        break

    if guess != number and lives > 0:
        print("That's not it, try again!")

    lives -= 1

if lives == 0:
    print("You lose!")