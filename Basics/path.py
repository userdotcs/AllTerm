import os


def userpath():
    return os.path.expanduser('~')


def back(path):
    return os.path.dirname(path)
