text = list(input())
power = 0
index = 0
last_list = []

for index in range(len(text)):

    if text[index] == ">":
        power += int(text[index + 1])
        while power > 0 and index < (len(text) - 1):
            if not text[index + 1] == ">":
                index += 1
                text[index] = "remove"
                power -= 1
            else:
                break

for el in text:
    if el != "remove":
        last_list.append(el)

print(*last_list, sep="")



