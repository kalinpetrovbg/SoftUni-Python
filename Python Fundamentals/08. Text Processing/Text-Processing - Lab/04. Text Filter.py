words = input().split(", ")
text = input()

for word in words:
    if word in text:
        text = text.replace(word, "*" * len(word))

print(text)