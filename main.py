from running_system import run_command
import console

while True: # Repeats until quit
    command = input(console.directory + "> ") # Get command
    run_command(command) # Run command
