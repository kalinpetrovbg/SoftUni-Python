import re

pattern = r"((?<=^_)|(?<=\s_))[a-zA-Z0-9]+\b"
data = input()

result = [el.group() for el in re.finditer(pattern, data)]

print(*result, sep=",")
