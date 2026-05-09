import sys


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
            if command[5:] in ("echo","exit","type"):
                sys.stdout.write(f"{command[5:]} is a shell builtin\n")
            else:
                sys.stdout.write(f"{command}: not found\n")


        else:
            sys.stdout.write(f"{command}: command not found\n")



if __name__ == "__main__":
    main()
