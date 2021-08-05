# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.
# Hard-code a word that needs to be guessed in the script
# Print an explanation to the user
# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"
# Ask for user input
# Allow only single-character alphabetic input
# Create a counter for how many tries a user has
# Keep asking them for their guess until they won or lost
# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"
# Display a winning message and the full word if they win
# Display a losing message and quit the game if they don't make it

print("Welcome to Hang-Man")
print("You will have three strikes to guess the secret word.")

strikes = 3
word = "investment"
solution = "__________" # 10 characters

# As long as they have some strikes left, play the game
while strikes != 0:

    # Check to see if the guess is a single letter
    guess = input("enter your guess: ")
    if len(guess) != 1 or guess.isalpha() != True:
        print("Please enter a letter.")
        continue

# Check if guess is in the word.
    if guess in word:
        # solution = solution.split()
        # If it is in the word, add it to the displayed solution
        for location in range(len(word)):
            if word[location] == guess and location == 0:
                solution = guess + solution[location + 1:]
            elif word[location] == guess:
                solution = solution[0:location] + guess + solution[location + 1:]

    else:
# if it isn't in the word, take away a strike
        strikes -= 1
        if strikes > 0:
            print(f"That letter isn't in the word.  You still have {strikes} strikes left.")
# If they run out of strikes, losing message
        elif strikes == 0:
            print("Wrong answer! You are all out of strikes, game over!")
            break

# if it is the last letter, winning message
    if solution == word:
        print(f"Hangman: {solution}")
        print("You have solved the puzzle! You win!")
        break

# display their current strikes and state of the solution
    print(f"Hangman: {solution}  strikes: {'* ' *strikes}")