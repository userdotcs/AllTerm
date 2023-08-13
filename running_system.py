from os import listdir, path
from errors import NotNamespaceOrCommand, NotNamespace

all_commands = {}

for i in listdir("commands"): # Auto in 'commands' folder
    if path.isfile("commands/" + i):
        command_group = i.replace(".py", "")
        exec(
            f"from commands.{command_group} import command_list\nall_commands.update({{'{command_group}':command_list}})"
        ) # Import and add to command and namespaces list command or namespace


def run_command(command):
    command_args = command.split()
    command_group = []

    parameters = []
    for i in command_args: # Parameter detective
        if i.startswith("-"):
            param = i[1 : len(i)]
            parameters.append(param)
        else:
            command_group.append(i)

    command = all_commands
    for group in command_group: # Auto in namespace directory in first of command
        if type(command) != dict:
            NotNamespace().alert()
            return
        if group in command:
            command = command[group]
        else:
            NotNamespaceOrCommand(group).alert()
            return

    command.execute(parameters)
