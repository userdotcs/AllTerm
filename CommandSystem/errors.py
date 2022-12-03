class AllError:
    def __init__(self, msg):
        print(msg)


class CommandNotFoundError(AllError):
    pass


class PathNotDirError(AllError):
    pass


class WrongTypeError(AllError):
    pass

class DirectoryNotFoundError(AllError):
    pass
