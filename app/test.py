import re

# t = "echo hello    world"
# print(t[5:].split(""))


text = "echo hello world"

parts = re.split(r"\s+", text[5:])
print(" ".join(parts))
