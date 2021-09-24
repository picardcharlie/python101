# Build a CLI RPG game following the instructions from the course.

# Ask the player for their name.

# Display a message that greets them and introduces them to the game world.

# Present them with a choice between two doors.

# If they choose the left door, they'll see an empty room.

# If they choose the right door, then they encounter a dragon.
 
# In both cases, they have the option to return to the previous room or interact further.

# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.

# When encountering the dragon, they have the choice to fight it.

# If they have the sword from the other room, then they will be able to defeat it and win the game.

# If they don't have the sword, then they will be eaten by the dragon and lose the game.

#https://dev.to/picardcharlie/my-new-cli-rpg-agj 
#quick write up on it.

# weather API URL = "https://www.metaweather.com/api/"

import requests


print("Welcome to Xin Shijie!")
while True:
    player_name_input = input("Please traveler, tell us your name so we can give you one from ours: ")
    if type(player_name_input) == str and len(player_name_input) >= 2 and len(player_name_input) <= 40:
        break
    else:
        print("Your name must be between 2 and 40 characters in length and use a character in it, please.")

name_min = len(player_name_input)
name_max = name_min
generate_name_url = f"https://uzby.com/api.php?min={name_min}&max={name_max}"
name_request = requests.get(generate_name_url)
character_name = name_request.text

print(f"We are so pleased to meet you {character_name}.")

# Weather API to get the current "random" weather from Hong Kong. woeid	2165352
weather_url = "https://www.metaweather.com/api/location/2165352/"
response = requests.get(weather_url).json()

current_weather = response['consolidated_weather'][0]['weather_state_name']

print(f"You arrive on a {current_weather.lower()} day, ready to enjoy your pancake picnic.")


input("...")
input("...")
input(".....?")

sword = False
dragon = True
room = 1

while dragon == True:
    if room == 1: #First room with two doors
        print("You find yourself facing two doors.")
        door = input("Do you enter the left or right: ")
        if door == "left":
            room = 2

        elif door == "right":
            room = 3

        else:
            print("Please pick a door!")

    if room == 2: #The empty room
        print("You find yourself in an empty room.")
        room_action = input("What would you like to do: ")
        if room_action == "leave":
            print("You leave the room.")
            room = 1

        elif room_action == "explore":
            print("You find a sword laying on the floor.")
            sword = True

        else:
            print("Maybe explore the room?")

    if room == 3: #Dragon room
        dragon_action = input("You find yourself facing a dragon, do you fight or run: ")
        if dragon_action == "fight" and sword == False:
            input("You charge at the dragon and it annihilates you...")
            print("Game over")
            break

        elif dragon_action == "fight" and sword == True:
            input("You charge at the dragon, leaping through the air..")
            input("Slashing your sword across the dragon, eviserating the beast.")
            print("You win!")
            break

        elif dragon_action == "run":
           input("You run out of the room, barely escaping certain death.")
           room = 1
        else:
            input("That won't work this time.")
