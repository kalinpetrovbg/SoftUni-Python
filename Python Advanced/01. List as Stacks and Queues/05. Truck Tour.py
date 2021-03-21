pumps = int(input())
data = [[int(x) for x in input().split()] for _ in range(pumps)]
found = False

for index in range(pumps):
    current = 0
    if found:
        break

    for turn in range(pumps):
        current += data[0 + turn][0]
        if current < data[0 + turn][1]:
            removed = data.pop(0)
            data.append(removed)
            break
        else:
            current -= data[0 + turn][1]
            if turn == pumps - 1:
                found = True
                print(index)