word = input()
match = input()

result = ""

while word in match:
    match = match.replace(word, "")

print(match)