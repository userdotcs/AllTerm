from command import Command, Req


def quit(p: list):
    exit(int(p[0]))


command_list = Command(quit, quit, quit, [0])
