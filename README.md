Minimum required python version: 3.6

# AllTerm sys commands
AllTerm have this commands:
- 'mkdir' allows you to select path.
- 'up' allows to go to the parent directory.
- 'quit' will close the program.

# How to improve Allterm?
Adding our own command to AllTerm is simple! Write an AllTerm library file and put it in the 'commands' folder. A library file should look like this:

```python
# mkdir.py
from command import Command, Req
from errors import PathNotFound
import console, os


def mkdir(p: list):
    new = os.path.join(console.directory, p[0])
    if os.path.exists(new):
        console.directory = new
        os.chdir(new)
    elif os.path.exists(p[0]):
        console.directory = p[0]
        os.chdir(p[0])
    else:
        PathNotFound(new).alert()
        return


command_list = Command(mkdir, mkdir, mkdir, [Req()])
```

'Command' is base class for commands. 'errors' module is basic error module of program. 'console' module have console infos.

In example, you will use it with `mkdir -desktop`

If you want add a command group, file should look like this:
```python
# sys.py
from command import Command, Req
from errors import PathNotFound
import console, os


def mkdir(p: list):
    new = os.path.join(console.directory, p[0])
    if os.path.exists(new):
        console.directory = new
        os.chdir(new)
    elif os.path.exists(p[0]):
        console.directory = p[0]
        os.chdir(p[0])
    else:
        PathNotFound(new).alert()
        return


def up(p: list):
    new = os.path.dirname(console.directory)
    console.directory = new
    os.chdir(new)


command_list = {
  "mkdir": Command(mkdir, mkdir, mkdir, [Req()]),
  "up": Command(up, up, up, [])
}
```
In example, you will use it with `sys mkdir -desktop` or `sys up`

# What operating systems does AllTerm run on?
AllTerm run on Windows, Linux and MacOS.
