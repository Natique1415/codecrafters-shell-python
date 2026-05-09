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

        else:
            sys.stdout.write(f"{command}: command not found\n")



if __name__ == "__main__":
    main()
