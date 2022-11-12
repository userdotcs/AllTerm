from CommandSystem.commands import *
from CommandSystem.errors import *

commands = [
    BackCom(),
    ExitCom(),
    MkdCom()
]


def run_com(com):
    for command in commands:
        if command.arg == com:
            command.run()
            return
    CommandNotFoundError(f"'{com}' command not found.")
