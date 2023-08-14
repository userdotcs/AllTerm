from command import Command, Req
from errors import PathNotFound
import console, os


def mkdir(p: list):
    new = os.path.join(console.directory, p[0]) # Path joining
    if os.path.exists(new):
        console.directory = new
        os.chdir(new)
    elif os.path.exists(p[0]):
        console.directory = p[0]
        os.chdir(p[0])
    else:
        PathNotFound(new).alert()
        return


command_list = Command(mkdir, mkdir, mkdir, [Req()])
