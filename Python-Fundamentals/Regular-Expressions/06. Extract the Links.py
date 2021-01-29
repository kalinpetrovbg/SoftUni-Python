import re

text = input()
pattern = r"(^|(?<=\s))w{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+($|(?=\s))"

while text:

    for el in re.finditer(pattern, text):
        print(el.group())

    text = input()