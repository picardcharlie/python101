# Write a script that renames all the files in a folder, giving them a default name and an incrementing counter.

import pathlib
import sys

# Warn about file renaming so I don't do it to myself mostly.
print("This script will rename everything in the current folder.")
warning = input("  Would you like to continue? Y/N")

if warning.lower() == "n" or warning.lower() == "no":
    sys.quit()

#Ask for new file name then go through every file and rename it with a number.

new_name = input("What is new name: ")
number = 1

for file in pathlib.Path().cwd():

# ignore it if it's a directory
    if file.is_dir() == True:
        pass

    replace = new_name + "-" + str(number)
    file.rename(replace)
    number += 1