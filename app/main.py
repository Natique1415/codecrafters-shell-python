import sys
import os

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

            # now to check each dir in PATH
            else:
                directories = os.environ.get("PATH").split(os.pathsep)
                command_name = command[5:].strip()
                file_name = command_name + ".exe"

                for directory in directories:
                    full_path = os.path.join(directory, file_name)
                    if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                        sys.stdout.write(f"{command_name} is {full_path}\n")

                sys.stdout.write(f"{command_name}: not found\n")

        else:
            sys.stdout.write(f"{command}: command not found\n")


if __name__ == "__main__":
    main()
