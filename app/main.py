import sys
import os
import shlex
import subprocess

BUILTIN_COMMANDS = ("echo", "exit", "type", "pwd", "cd")
HOME_DIRECTORY = os.path.expanduser("~")
DIRECTORIES = os.environ.get("PATH").split(
    os.pathsep
)  # pyright: ignore[reportOptionalMemberAccess]


def main():
    while True:
        sys.stdout.write("$ ")
        command = input().strip()

        cmd = shlex.split(command)

        if cmd[0] == "exit":
            sys.exit()

        elif cmd[0] == "echo":
            if cmd[-2] in (">", "1>"):
                args = cmd[1 : len(cmd) - 2]
                with open(cmd[-1], "w") as outfile:
                    subprocess.run([cmd[0]] + args, stdout=outfile)

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

            # then we check for the presence of > or 1>
            elif cmd[-2] in (">", "1>"):
                args = cmd[1 : len(cmd) - 2]
                with open(cmd[-1], "w") as outfile:
                    subprocess.run([command_name] + args, stdout=outfile)
                    # file.write(" ".join(cmd[1 : len(cmd) - 2]))

            # contains no > or 1> so run as already do
            else:
                args = cmd[1:]
                subprocess.run([command_name] + args)


# Checks if command exit in the PATH and does it executable permissions
def does_command_exist(command_name: str):
    for directory in DIRECTORIES:
        full_path = os.path.join(directory, command_name)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return full_path
    return "DOES_NOT_EXIST"


if __name__ == "__main__":
    main()
