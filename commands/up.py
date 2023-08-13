from command import Command, Req
import console, os


def up(p: dict):
    new = os.path.dirname(console.directory)
    console.directory = new # Set default path of console to up
    os.chdir(new) # Set default path of program to up 


command_list = Command(up, up, up, []) # Import info
