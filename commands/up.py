from command import Command
import console, os


def up(p: list):
    for i in range(int(p[0])):
        new = os.path.dirname(console.directory)
        console.directory = new # Set default path of console to up
        os.chdir(new) # Set default path of program to up 


command_list = Command(up, up, up, [1]) # Import info
