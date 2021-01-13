text = input().upper()
result = ""
final = ""
num = 0

for index, char in enumerate(text):
    if not char.isnumeric():
        result += char
    else:
        if num != 0:
            num = 0
            continue
        if index < len(text) - 1:
            if text[index + 1].isdigit():
                second = text[index + 1]
                num = char + second
                result = int(num) * result
            else:
                result = int(text[index]) * result
        if index == len(text) - 1:
            result *= int(char)

        final += result
        result = ""

print(f"Unique symbols used: {len(set(final))}")
print(final)