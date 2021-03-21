text = input()
result = []

for index in range(len(text)):
    if text[index].isupper():
        result.append(index)

print(result)