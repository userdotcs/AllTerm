from CommandSystem.commands import *
from CommandSystem.errors import *

commands = [
    BackCom(),
    ExitCom()
]


def run_com(com):
    for command in commands:
        if command.arg == com:
            command.run()
            return
    CommandNotFoundException(f"'{com}' command not found.")
