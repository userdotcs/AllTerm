from CommandSystem.command import Command
import Basics.path as p
import Terminal.terminal_info as ti


class BackCom(Command):
    def __init__(self):
        self.arg = 'back'

    def run(self):
        ti.cur_dir = p.back(ti.cur_dir)


class ExitCom(Command):
    def __init__(self):
        self.arg = 'exit'

    def run(self):
        exit()
