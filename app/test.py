import re

text1 = "echo 'hello    world'"
text2 = "echo 'hello''world'"
text3 = "echo hello''world"

res1 = re.findall(r"'([^']*)'", text1[5:])
res2 = re.findall(r"'([^']*)'", text2[5:])
res3 = re.findall(r"'([^']*)'", text3[5:])
print("".join(res1))
print("".join(res2))
# print("".join(res3))
print(re.findall(r"'([^']*)'", text3))
