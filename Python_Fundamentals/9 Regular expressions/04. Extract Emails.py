import re

text = input()
pattern = r"(^|(?<=\s))[a-zA-Z\d]+[\._-]?[a-zA-Z\d]+@[a-zA-Z]+\-?[a-zA-Z]+(\.[a-zA-Z]+)+"
# pattern = r"(^|(?<=\s))[a-zA-Z\d]+[\._-]?[a-zA-Z\d]+@[a-zA-Z]+\-?[a-zA-Z]+(\.[a-zA-Z]+)+($|(?=\s))"

result = re.finditer(pattern, text)
for element in result:
    print(element.group())
