class AllError:
    def __init__(self, msg):
        print(msg)


class CommandNotFoundException(AllError):
    pass
