gifts = input().split()
gift_list = []
length = len(gifts)

for each in gifts:
    gift_list.append(each)

while True:
    command = input().split()

    if command[0] == "OutOfStock":
        if command[1] in gift_list:
            element = command[1]
            gift_list = ["None" if x == element else x for x in gift_list]
        else:
            continue

    if command[0] == "Required":
        if 0 < int(command[2]) < length:  # if it is valid
            indexing = int(command[2])  # 2
            new_word = command[1]  # Spoon
            gift_list[indexing] = new_word  # replace index 2 with Spoon
        else:
            continue

    if command[0] == "JustInCase":
        gift_list.pop()
        gift_list.append(command[1])

    if command[1] == "Money":
        break

xy = gift_list
while "None" in xy: xy.remove("None")   # using lambda removing repetitions

print(* gift_list, sep=" ")
