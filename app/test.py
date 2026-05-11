import shlex

command = "type echo"
cmd = shlex.split(command)
command_name = cmd[1:]

print(cmd)
print(command_name)
