from Basics.path import userpath
from CommandSystem.errors import WrongTypeError

cur_dir = userpath()


def get_int_terminal_input(q):
    inp = input(f"{q}> ")
    try:
        return int(inp)
    except:
        WrongTypeError("Wrong input.")


def get_str_terminal_input(q):
    return input(f"{q}> ")
