text = input()
output = {}

for char in text:
    if char != " ":
        if char not in output:
            output[char] = 0
        output[char] += 1

for letter, number in output.items():
    print(f"{letter} -> {number}")
