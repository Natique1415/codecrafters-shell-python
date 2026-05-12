from contextlib import redirect_stdout

with open("help.txt", "w") as f:
    with redirect_stdout(f):
        print("it now prints to `help.text`")
