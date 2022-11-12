import os
from CommandSystem.errors import *


def userpath():
    return os.path.expanduser('~')


def back(path):
    return os.path.dirname(path)


def ispath(path):
    return os.path.isdir(path)


def listpath(path):
    if ispath(path):
        return os.listdir(path)
    else:
        PathNotDirError(f"'{path}' is not directory.")
