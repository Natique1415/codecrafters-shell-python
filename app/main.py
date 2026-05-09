import sys


def main():
    while True:
        sys.stdout.write("$ ")
        command = input().strip()
        if command.lower() == "exit":
            sys.exit()
        else:
            sys.stdout.write(f"{command}: command not found\n")



if __name__ == "__main__":
    main()
