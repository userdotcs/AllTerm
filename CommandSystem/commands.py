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


class MkdCom(Command):
    def __init__(self):
        self.arg = "mkd"

    def run(self):
        pathlist = p.listpath(ti.cur_dir)
        a = 1
        for path in pathlist:
            print(f"{a}) {path}")
            a += 1

        ti.cur_dir += f"/{pathlist[ti.get_int_terminal_input('Numb') - 1]}"
