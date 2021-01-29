import re

text = input()
pattern = f"\\b{input()}\\b"

result = re.findall(pattern, text, re.IGNORECASE)

print(len(result))
