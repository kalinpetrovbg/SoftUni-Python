text_1 = input()
text_2 = input()
text = text_1

for x in range(len(text_1)):
    s1 = text_1[x + 1: len(text_1)]
    s2 = text_2[0:x + 1]
    if s2 + s1 == text:
        continue
    text = s2 + s1
    print(text)
