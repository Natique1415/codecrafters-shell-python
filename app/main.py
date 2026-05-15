import sys
import os
import shlex
import subprocess
import readline

BUILTIN_COMMANDS = ("echo", "exit", "type", "pwd", "cd")
HOME_DIRECTORY = os.path.expanduser("~")
PATH_DIRECTORY = os.environ.get("PATH").split(os.pathsep)  # type: ignore


# auto-complete code starts


def completer(text, state):
    # Filter options that start with the input text
    matches = [o for o in COMMANDS_TO_AUTOCOMPLETE if o.startswith(text)]

    # Return the match corresponding to the current state
    try:
        return matches[state] + " "
    except IndexError:
        return None


def executable_autocomplete_list() -> list[str]:
    executables = []
    for directory in PATH_DIRECTORY:

        if os.path.exists(directory):
            for filename in os.listdir(directory):
                file_path = os.path.join(directory, filename)
                if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
                    executables.append(filename)

    return executables


# def file_autocomplete_list() -> list[str]:
#     files = []
#     for filename in os.listdir("."):
#         files.append(filename)


#     return files
def file_autocomplete_list() -> list[str]:
    files_items = []
    for root, dirs, files in os.walk("."):
        for filename in files:
            # Get the full path and convert it to a relative path
            relative_path = os.path.relpath(os.path.join(root, filename), ".")
            # print(f"Name: {filename} | Relative Path: {relative_path}")
            files_items.append(relative_path)

    # return files_items
    return files_items


COMMANDS_TO_AUTOCOMPLETE = (
    [
        "echo",
        "exit",
    ]
    + executable_autocomplete_list()
    + file_autocomplete_list()
)
readline.set_completer(completer)  # type: ignore
readline.parse_and_bind("tab: complete")  # type: ignore
# auto-complete code ends


def main():
    while True:
        command = input("$ ").strip()

        # cmd[0] cmd name and cmd[1:] the args
        cmd = shlex.split(command)

        if cmd[0] == "exit":
            sys.exit()

        elif cmd[0] == "echo":
            args = cmd[1 : len(cmd) - 2]

            if cmd[-2] in (">", "1>"):
                redirect_output(cmd[0], args, cmd[-1])

            elif cmd[-2] in (">>", "1>>"):
                with open(cmd[-1], "a") as file:
                    subprocess.run([cmd[0]] + args, stdout=file)

            elif cmd[-2] == "2>>":
                args = cmd[1 : len(cmd) - 2]
                with open(cmd[-1], "a") as file:
                    subprocess.run([cmd[0]] + args, stderr=file)

            elif cmd[-2] == "2>":
                redirect_error(cmd[0], args, cmd[-1])

            else:
                sys.stdout.write(f"{" ".join(cmd[1:])}\n")

        elif cmd[0] == "pwd":
            sys.stdout.write(f"{os.getcwd()}\n")

        elif cmd[0] == "cd":
            directory = cmd[1]
            if directory == "~":
                os.chdir(HOME_DIRECTORY)
            elif os.path.exists(directory):
                os.chdir(directory)
            else:
                sys.stdout.write(f"cd: {directory}: No such file or directory\n")

        elif cmd[0] == "type":
            if cmd[1] in BUILTIN_COMMANDS:
                sys.stdout.write(f"{cmd[1]} is a shell builtin\n")

            # now to check each dir in PATH for the program ( making sure it has executable permission )
            else:
                path_of_file = does_command_exist(cmd[1])
                if path_of_file == ("DOES_NOT_EXIST"):
                    sys.stdout.write(f"{cmd[1]}: not found\n")
                else:
                    sys.stdout.write(f"{cmd[1]} is {path_of_file}\n")

        elif cmd[0] in ("cls", "clear"):
            os.system("cls" if os.name == "nt" else "clear")

        else:
            command_name = cmd[0]
            # before anything, check if the command exist to begin with
            if does_command_exist(cmd[0]) == ("DOES_NOT_EXIST"):
                sys.stdout.write(f"{command}: command not found\n")

            # then we check for the presence of > or 1>( standard output )
            elif cmd[-2] in (">", "1>"):
                args = cmd[1 : len(cmd) - 2]
                redirect_output(command_name, args, cmd[-1])

            elif cmd[-2] in (">>", "1>>"):
                args = cmd[1 : len(cmd) - 2]
                with open(cmd[-1], "a") as file:
                    subprocess.run([cmd[0]] + args, stdout=file)

            elif cmd[-2] == "2>":
                args = cmd[1 : len(cmd) - 2]
                redirect_error(command_name, args, cmd[-1])

            elif cmd[-2] == "2>>":
                args = cmd[1 : len(cmd) - 2]
                with open(cmd[-1], "a") as file:
                    subprocess.run([cmd[0]] + args, stderr=file)

            # contains no > or 1> so run as already do
            else:
                args = cmd[1:]
                subprocess.run([command_name] + args)


# Checks if command exit in the PATH and does it executable permissions
def does_command_exist(command_name: str) -> str:
    for directory in PATH_DIRECTORY:
        full_path = os.path.join(directory, command_name)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return full_path
    return "DOES_NOT_EXIST"


def redirect_output(command_name: str, args: list[str], file_path: str):
    with open(file_path, "w") as file:
        subprocess.run([command_name] + args, stdout=file)


def redirect_error(command_name: str, args: list[str], file_path: str):
    with open(file_path, "w") as file:
        subprocess.run([command_name] + args, stderr=file)


if __name__ == "__main__":
    main()
