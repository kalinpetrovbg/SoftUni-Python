import re

text = input()
line = []

while text:
    pattern = r"\d+"
    result = re.findall(pattern, text)
    line.extend(result)
    text = input()

print(*line, sep=" ")