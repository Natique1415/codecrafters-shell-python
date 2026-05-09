import sys
import os
import subprocess

BUILTIN_COMMANDS = ("echo", "exit", "type")


def main():
    while True:
        sys.stdout.write("$ ")
        command = input().strip()

        if command == "exit":
            sys.exit()

        elif command.startswith("echo "):
            message = command[5:]
            sys.stdout.write(f"{message}\n")

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
                subprocess.run([path_of_file] + args)


def does_command_exist(command_name: str):
    directories = os.environ.get("PATH").split(os.pathsep)
    # command_name = command[5:].strip()
    # command_exist = False

    for directory in directories:
        full_path = os.path.join(directory, command_name)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return full_path
            # sys.stdout.write(f"{command_name} is {full_path}\n")
            # command_exist = True
            break
    return "DOES_NOT_EXIST"
    # if command_exist == False:
    #     sys.stdout.write(f"{command_name}: not found\n")


if __name__ == "__main__":
    main()
