n = int(input())
commands = input().split()
matrix = [[x for x in input().split()] for _ in range(n)]
pos = []
total_coals = 0
collected = 0

for i in range(n):
    for j in range(n):
        if matrix[i][j] == "s":
            pos.extend((i, j))
        if matrix[i][j] == "c":
            total_coals += 1

while commands:
    if commands[0] == "up":
        if 0 <= pos[0] - 1 < n and 0 <= pos[1] < n:
            pos[0] -= 1
            if matrix[pos[0]][pos[1]] == "e":
                print(f"Game over! {tuple(pos)}")
                total_coals = collected
                break
            elif matrix[pos[0]][pos[1]] == "s":
                matrix[pos[0]][pos[1]] = "*"
            elif matrix[pos[0]][pos[1]] == "c":
                collected += 1
                matrix[pos[0]][pos[1]] = "*"


    elif commands[0] == "down":
        if 0 <= pos[0] + 1 < n and 0 <= pos[1] < n:
            pos[0] += 1
            if matrix[pos[0]][pos[1]] == "e":
                print(f"Game over! {tuple(pos)}")
                total_coals = collected
                break
            elif matrix[pos[0]][pos[1]] == "s":
                matrix[pos[0]][pos[1]] = "*"
            elif matrix[pos[0]][pos[1]] == "c":
                collected += 1
                matrix[pos[0]][pos[1]] = "*"

    elif commands[0] == "left":
        if 0 <= pos[0] < n and 0 <= pos[1] - 1 < n:
            pos[1] -= 1
            if matrix[pos[0]][pos[1]] == "e":
                print(f"Game over! {tuple(pos)}")
                total_coals = collected
                break
            elif matrix[pos[0]][pos[1]] == "s":
                matrix[pos[0]][pos[1]] = "*"
            elif matrix[pos[0]][pos[1]] == "c":
                collected += 1
                matrix[pos[0]][pos[1]] = "*"

    elif commands[0] == "right":
        if 0 <= pos[0] < n and 0 <= (pos[1] + 1) < n:
            pos[1] += 1
            if matrix[pos[0]][pos[1]] == "e":
                print(f"Game over! {tuple(pos)}")
                total_coals = collected
                break
            elif matrix[pos[0]][pos[1]] == "s":
                matrix[pos[0]][pos[1]] = "*"
            elif matrix[pos[0]][pos[1]] == "c":
                collected += 1
                matrix[pos[0]][pos[1]] = "*"

    if collected == total_coals:
        print(f"You collected all coals! {tuple(pos)}")
        break

    commands.pop(0)

if total_coals > collected:
    print(f"{total_coals - collected} coals left. {tuple(pos)}")