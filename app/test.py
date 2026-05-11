import re

# t = "echo hello    world"
# print(t[5:].split(""))


def parse_word(pharse: str):
    i = 0
    word = ""
    while i < len(pharse):
        if pharse[i] == "'":
            i = i + 1
            while pharse[i] != "'":
                word = word + pharse[i]

                i = i + 1
    print(word)


test = "echo 'hello  world'"
print(parse_word(test[5:]))
