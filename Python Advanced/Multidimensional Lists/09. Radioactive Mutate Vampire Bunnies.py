rows, cols = [int(x) for x in input().split()]
matrix = [list(input()) for _ in range(rows)]
commands = list(input())
pos = []
dead = False

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == "P":
            pos.append(i)
            pos.append(j)
            matrix[i][j] = "."

while commands:

    if commands[0] == "U":
        pos[0] -= 1
    elif commands[0] == "D":
        pos[0] += 1
    elif commands[0] == "L":
        pos[1] -= 1
    elif commands[0] == "R":
        pos[1] += 1

    for y in range(rows):
        for z in range(cols):
            if matrix[y][z] == "B":
                if 0 <= y+1 < rows and 0 <= z < cols:
                    if matrix[y+1][z] != "B":
                        matrix[y+1][z] = "C"
                if 0 <= y - 1 < rows and 0 <= z < cols:
                    if matrix[y-1][z] != "B":
                        matrix[y-1][z] = "C"
                if 0 <= y < rows and 0 <= z + 1 < cols:
                    if matrix[y][z+1] != "B":
                        matrix[y][z+1] = "C"
                if 0 <= y < rows and 0 <= z - 1 < cols:
                    if matrix[y][z - 1] != "B":
                        matrix[y][z-1] = "C"

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "C":
                matrix[i][j] = "B"

    if 0 > pos[0] or 0 > pos[1] or pos[0] >= rows or pos[1] >= cols:
        if commands[0] == "U":
            pos[0] += 1
        elif commands[0] == "D":
            pos[0] -= 1
        elif commands[0] == "L":
            pos[1] += 1
        elif commands[0] == "R":
            pos[1] -= 1
        dead = False
        break

    if matrix[pos[0]][pos[1]] == "B":
        dead = True
        break

    commands.pop(0)

print("\n".join("".join(map(str, x)) for x in matrix))
if not dead:
    print(f"won: {pos[0]} {pos[1]}")
else:
    print(f"dead: {pos[0]} {pos[1]}")
