import shlex

command = "echo 'world' hello"
tokens = shlex.split(command)

print(tokens)
