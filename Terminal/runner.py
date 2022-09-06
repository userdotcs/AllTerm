from CommandSystem.commands import *
from CommandSystem.errors import *

commands = [
    BackCom(),
    ExitCom()
]


def run_com(com):
    try:
        for command in commands:
            if command.arg == com:
                command.run()
                return
        raise CommandNotFoundException(f"'{com}' command not found.")
    except CommandNotFoundException as e:
        print(e)
