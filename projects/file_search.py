# Write a script that searches a folder you specify (as well as its subfolders, up to two levels deep)
# and compiles a list of all .jpg files contained in there.
# The list should include the complete path of each .jpg file.

# If you are feeling bold, create a list containing each type of file extension you find in the folder.
# Start with a small folder to make it easy to check whether your program is working correctly. Then search a bigger folder.
# This program should work for any specified folder on your computer.

import pathlib

# copy and pasted the lab, why reinvent all of the wheel?

# path to the current directory
current_directory = pathlib.Path().cwd()

for files in current_directory.iterdir():
#if it's a .jpg file, print the name.
    if files.suffix == ".jpg":
        print(files)

# if it's a directory, change to it
    if files.is_dir() == True:
        sub_directory = currentdirectory.joinpath(files.name)

# go through directory and print all .jpg
        for sub_files in sub_directory.iterdir():

            if sub_files.suffix == ".jpg":
                print(sub_files)

# Check the sub-sub directory for them.
            if sub_files.is_dir() == True:
                basement_files = sub_directory.joinpath(sub_files.name)

                for base in basement_files.iterdir():

                    if base.suffix == ".jpg":
                        print(base)