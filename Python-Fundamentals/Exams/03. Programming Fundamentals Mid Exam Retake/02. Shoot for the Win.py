targets = [int(el) for el in input().split()]

while True:
    command = input()
    if command == "End":
        break
    command = int(command)

    if command < len(targets):
        shooting_index = targets[command]
        targets.pop(command)

        for i in range(len(targets)):
            if targets[i] > shooting_index:
                targets[i] -= shooting_index
            else:
                if targets[i] != -1:
                    targets[i] += shooting_index

        targets.insert(command, -1)

print(f"Shot targets: {len([_ for _ in targets if _ == -1])} -> {' '.join(list(map(str, targets)))}")