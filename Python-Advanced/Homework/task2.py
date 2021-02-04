import string

punctuation = [",", ".", "-", "!", "?", ":", ";", "'"]
alphabet = list(string.ascii_lowercase)

with open("text2.txt", "r") as file:
    lines = file.readlines()

    for index in range(len(lines)):
        num_symbols = 0
        alpha_counter = 0
        for symbol in punctuation:
            if symbol in lines[index]:
                num_symbols += lines[index].count(symbol)
        for letter in lines[index].lower():
            if letter in alphabet:
                alpha_counter += 1
        result = f"Line {index + 1}: " + lines[index][:-1] + f"({alpha_counter})({num_symbols})"
        print(result)


# print("== The result should be: ==")
# print("Line 1: -I was quick to judge him, but it wasn't his fault. (37)(4)")
# print("Line 2: -Is this some kind of joke?! Is it? (24)(4)")
# print("Line 3: -Quick, hide here. It is safer. (22)(4)")
