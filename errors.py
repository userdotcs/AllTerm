class Error:
    msg: str
    def alert(self):
        print(self.msg)


class PathNotFound(Error):
    def __init__(self, path):
        self.msg = f"'{path}' is not found."


class MissingParameter(Error):
    def __init__(self):
        self.msg = "Missing parameter."


class MoreParameters(Error):
    def __init__(self):
        self.msg = "More parameter."


class NotNamespaceOrCommand(Error):
    def __init__(self, command):
        self.msg = f"'{command}' is not namespace or command."


class NotNamespace(Error):
    def __init__(self):
        self.msg = f"Not namespace."