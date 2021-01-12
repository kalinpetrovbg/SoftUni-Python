text = input()
result = ""

for index in range(len(text)):
    if index == len(text) - 1:
        break
    if text[index] != text[index + 1]:
        result += text[index]

last = text[-1]
print(result + last)