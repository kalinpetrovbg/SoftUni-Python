targets = [int(el) for el in input().split()]
command = input()

while not command == "End":
    types, index, power = command.split()
    index = int(index)
    power = int(power)

    if types == "Shoot":
        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)

    elif types == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, power)
        else:
            print("Invalid placement!")

    elif types == "Strike":
        range_down = index - power
        range_up = index + power
        if (range_down >= 0) and (range_up < len(targets)):
            del targets[range_down:range_up + 1]

        else:
            print("Strike missed!")

    command = input()

print("|".join([str(el) for el in targets]))
