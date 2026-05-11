# t = "echo hello    world"
# print(t[5:].split(""))


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


test = "echo 'script     test' 'example''hello' world''shell"
print(parse_word(test[5:]))
