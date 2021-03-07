n = int(input())
matrix = [[x for x in input().split()] for _ in range(n)]
pos = []
total = 0
path = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] == "P":
            pos.extend((i, j))

while True:
    command = input()

    if command == "up" and pos[0] - 1 >= 0:
        pos[0] -= 1
        if matrix[pos[0]][pos[1]] == "X":
            total = total // 2
            print(f"Game over! You've collected {total} coins.")
            break
        else:
            total += int(matrix[pos[0]][pos[1]])
            new = pos.copy()
            path.append(new)

    elif command == "down" and pos[0] + 1 < n:
        pos[0] += 1
        if matrix[pos[0]][pos[1]] == "X":
            total = total // 2
            print(f"Game over! You've collected {total} coins.")
            break
        else:
            total += int(matrix[pos[0]][pos[1]])
            new = pos.copy()
            path.append(new)

    elif command == "right" and pos[1] + 1 < n:
        pos[1] += 1
        if matrix[pos[0]][pos[1]] == "X":
            total = total // 2
            print(f"Game over! You've collected {total} coins.")
            break
        else:
            total += int(matrix[pos[0]][pos[1]])
            new = pos.copy()
            path.append(new)

    elif command == "left" and pos[1] - 1 >= 0:
        pos[1] -= 1
        if matrix[pos[0]][pos[1]] == "X":
            total = total // 2
            print(f"Game over! You've collected {total} coins.")
            break
        else:
            total += int(matrix[pos[0]][pos[1]])
            new = pos.copy()
            path.append(new)

    else:
        total = total // 2
        print(f"Game over! You've collected {total} coins.")
        break

    if total > 100:
        print(f"You won! You've collected {total} coins.")
        break

print("Your path:")
print(*path, sep="\n")
