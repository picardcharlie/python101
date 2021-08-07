
import pathlib

# current location of the python script.
path = pathlib.Path().cwd()

# everything is an object in /Python/

# print out every file in a directory.
for filepath in path.iterdir():
    print(filepath.name)

# directory of the desktop
desktop = pathlib.Path("/home/monster/Desktop")

# print out everything in the desktop
for filepath in desktop.iterdir():
    print(filepath.name)

# filter by suffix with .suffix
for filepath in desktop.iterdir():
    print(filepath.suffix)

# print out all the .jpg files
for filepath in desktop.iterdir():
    if filepath.suffix == ".jpg":
        print(filepath.name)

# can create directories with mkdir() | glad this is all linux commands
new_path = pathlib.Path("/home/monster/Desktop/screenshots")
new_path.mkdir(exist_ok = True)
# exist_ok will check to see if the directory is there already or not.  If it is already there, it won't give an error.

# move files with .replace()
# oldpath.replace(newpath)

for filepath in desktop.iterdir():
    if filepath.suffix == ".jpg":
        new_filepath = new_path.joinpath(filepath.name)
        filepath.replace(new_filepath)
