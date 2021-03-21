text = input()
result = {}

for letter in text:
    if letter not in result:
        result[letter] = 1
    else:
        result[letter] += 1

for let, num in sorted(result.items(), key=lambda x: x[0]):
    print(f"{let}: {num} time/s")