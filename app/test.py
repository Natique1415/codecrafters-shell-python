import os
import sys

# Split the PATH environment variable into a list of directories
directories = os.environ.get("PATH").split(os.pathsep)
command = "type echo"
command_name = command[5:].strip()
file_name = command_name + ".exe"


for directory in directories:
    full_path = os.path.join(directory, file_name)
    if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
        sys.stdout.write(f"{command_name} is {full_path}")
