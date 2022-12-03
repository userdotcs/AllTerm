from CommandSystem.command import Command
import Basics.path as p
import Terminal.terminal_info as ti
from CommandSystem import errors as e

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
        if p.ispath(ti.cur_dir):
            pathlist = p.listpath(ti.cur_dir)
            a = 1
            for path in pathlist:
                print(f"{a}) {path}")
                a += 1

            numb = ti.get_int_terminal_input('Numb')
            if numb == 0:
                return
            else:
                ti.cur_dir += f"/{pathlist[numb - 1]}"
        else:
            e.PathNotDirError(f"'{ti.cur_dir}' is not directory.")


class MkdlCom(Command):
    def __init__(self):
        self.arg = "mkdl"

    def run(self):
        dir = ti.get_str_terminal_input("Long name of dir")
        if p.iscontains(dir):
            ti.cur_dir = dir
        else:
            e.DirectoryNotFoundError(f"'{dir}' not found.")
