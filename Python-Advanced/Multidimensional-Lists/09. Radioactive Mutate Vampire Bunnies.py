rows, cols = [int(x) for x in input().split()]
matrix = [list(input()) for _ in range(rows)]
commands = list(input())
pos = []

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == "P":
            pos.append(i)
            pos.append(j)
print(pos)

while commands:
    if commands[0] == "U":
        if 0 <= pos[0] - 1 < rows and 0 <= pos[1] < cols:
            pos[0] -= 1

    elif commands[0] == "D":
        if 0 <= pos[0] + 1 < rows and 0 <= pos[1] < cols:
            pos[0] += 1

    elif commands[0] == "L":
        if 0 <= pos[0] < rows and 0 <= pos[1] - 1 < cols:
            pos[1] -= 1

    elif commands[0] == "R":
        if 0 <= pos[0] < rows and 0 <= pos[1] + 1 < cols:
            pos[1] += 1



    commands.pop(0)