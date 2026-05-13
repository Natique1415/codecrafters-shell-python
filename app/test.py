import readline

# Your list of autocomplete options
OPTIONS = ("apple", "banana", "cherry", "date")


def completer(text, state):
    # Filter options that start with the input text
    matches = [o for o in OPTIONS if o.startswith(text)]

    # Return the match corresponding to the current state
    try:
        return matches[state]
    except IndexError:
        return None


# Register the completer and bind the Tab key
readline.set_completer(completer)
# For macOS (libedit), use: readline.parse_and_bind("bind ^I rl_complete")
readline.parse_and_bind("tab: complete")

while True:
    user_input = input("Enter a fruit: ")
    print(f"You entered: {user_input}")
