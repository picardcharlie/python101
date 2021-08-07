# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

import pathlib

# check currect directory for more files and and any .py files
# path.is_dir() checks to see if it's a file

# path to the python course
python101 = pathlib.Path("/home/monster/python/python101/")

for files in python101.iterdir():
    #if it's a .py file, print the name.
    if files.suffix == ".py":
        print(files)

    # if it's a directory, change to it
    if files.is_dir() == True:
        # print the directory name before listing the .py
        print(files.name)

        # go through directory and print all .py
        for sub_files in (python101.joinpath(files.name)).iterdir():
            if sub_files.suffix == ".py":
                print(f"   {sub_files.name}")