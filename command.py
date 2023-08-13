import platform
from errors import MissingParameter, MoreParameters


class Req:
    pass


class Command:
    def __init__(self, win_target, linux_target, darwin_target, default: list): # Get functions for Windows, Linux and Mac
        self.win_target = win_target
        self.linux_target = linux_target
        self.darwin_target = darwin_target
        self.default = default

    def execute(self, parameters: dict):
        if len(parameters) > len(self.default):
            MoreParameters().alert()
            return

        par = self.default
        for i in range(len(parameters)):
            if par[i] != parameters[i]:
                par[i] = parameters[i]

        for i in par:
            if type(par) == Req:
                MissingParameter().alert()
                return

        if platform.system() == "Windows":
            self.win_target(par)
        elif platform.system() == "Linux":
            self.linux_target(par)
        elif platform.system() == "Darwin":
            self.darwin_target(par)
