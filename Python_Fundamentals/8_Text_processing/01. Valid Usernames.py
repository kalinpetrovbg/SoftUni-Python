text = input().split(", ")

for word in text:
    if 3 <= len(word) <= 16:
        for ch in word:
            if not (ch.isalpha() or ch.isdigit() or ch == chr(45) or ch == chr(95)):
                break
        else:
            print(word)