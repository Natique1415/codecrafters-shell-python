import sys


def main():
    while True:
        sys.stdout.write("$ ")
        command = input().strip()
        sys.stdout.write(f"{command}: command not found")



if __name__ == "__main__":
    main()
