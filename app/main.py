import sys
import os
import re
import subprocess

BUILTIN_COMMANDS = ("echo", "exit", "type", "pwd", "cd")
HOME_DIRECTORY = os.path.expanduser("~")
DIRECTORIES = os.environ.get("PATH").split(os.pathsep)


def main():
    while True:
        sys.stdout.write("$ ")
        command = input().strip()

        if command == "exit":
            sys.exit()

        elif command.startswith("echo "):
            if "'" not in command[5:]:
                parts = re.split(r"\s+", command[5:])
                sys.stdout.write(f'{" ".join(parts)}\n')

            # containing at least one ' ( so assuming it contains the other ' as well )
            else:
                sys.stdout.write(f"{parse_word(command[5:])}\n")
                # string_inside_quotes = re.findall(r"'([^']*)'", command[5:])
                # if string_inside_quotes == [""]:
                #     sys.stdout.write(f'{command[5:].replace("'","")}\n')
                # else:
                # sys.stdout.write(f"{"".join(string_inside_quotes)}\n")

        elif command == "pwd":
            sys.stdout.write(f"{os.getcwd()}\n")

        elif command.startswith("cd "):
            directory = command[3:]
            if directory == "~":
                os.chdir(HOME_DIRECTORY)
            elif os.path.exists(directory):
                os.chdir(directory)
            else:
                sys.stdout.write(f"cd: {directory}: No such file or directory\n")

        elif command.startswith("type "):
            if command[5:] in BUILTIN_COMMANDS:
                sys.stdout.write(f"{command[5:]} is a shell builtin\n")

            # now to check each dir in PATH for the program ( making sure it has executable permission )
            else:
                command_name = command[5:]
                path_of_file = does_command_exist(command_name)
                if path_of_file == ("DOES_NOT_EXIST"):
                    sys.stdout.write(f"{command_name}: not found\n")
                else:
                    sys.stdout.write(f"{command_name} is {path_of_file}\n")

        else:
            command_name, args = command.split(" ")[0], command.split(" ")[1:]
            path_of_file = does_command_exist(command_name)

            if path_of_file == ("DOES_NOT_EXIST"):
                sys.stdout.write(f"{command}: command not found\n")
            else:
                subprocess.run([command_name] + args)


# Checks if command exit in the PATH and does it executable permissions
def does_command_exist(command_name: str):
    for directory in DIRECTORIES:
        full_path = os.path.join(directory, command_name)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return full_path
    return "DOES_NOT_EXIST"


def parse_word(phrase: str):
    i = 0
    word = ""
    while i < len(phrase):
        if phrase[i] == "'":
            j = i + 1
            while j < len(phrase) and phrase[j] != "'":
                word += phrase[j]
                j += 1

        i += 1

    return word


if __name__ == "__main__":
    main()
