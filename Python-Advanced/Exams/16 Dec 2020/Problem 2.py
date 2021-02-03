text = input()
n = int(input())
matrix = [list(input()) for _ in range(n)]
m = int(input())
pos = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] == "P":
            pos.extend((i, j))
            matrix[i][j] = "-"

for _ in range(m):
    command = input()

    if command == "down":
        if pos[0] + 1 < n:
            pos[0] += 1
            letter = matrix[pos[0]][pos[1]]
            if letter != "-":
                text += letter
                matrix[pos[0]][pos[1]] = "-"
        else:
            if len(text) > 0:
                text = text[:-1]
    elif command == "up":
        if 0 <= pos[0] - 1:
            pos[0] -= 1
            letter = matrix[pos[0]][pos[1]]
            if letter != "-":
                text += letter
                matrix[pos[0]][pos[1]] = "-"
        else:
            if len(text) > 0:
                text = text[:-1]
    elif command == "left":
        if 0 <= pos[1] - 1:
            pos[1] -= 1
            letter = matrix[pos[0]][pos[1]]
            if letter != "-":
                text += letter
                matrix[pos[0]][pos[1]] = "-"
        else:
            if len(text) > 0:
                text = text[:-1]
    elif command == "right":
        if pos[1] + 1 < n:
            pos[1] += 1
            letter = matrix[pos[0]][pos[1]]
            if letter != "-":
                text += letter
                matrix[pos[0]][pos[1]] = "-"
        else:
            if len(text) > 0:
                text = text[:-1]

matrix[pos[0]][pos[1]] = "P"

print(text)
print("\n".join(''.join(map(str, x)) for x in matrix))




