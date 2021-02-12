n = int(input())
m = int(input())
mines = [input().strip("()") for _ in range(m)]
matrix = [n * [0] for i in range(n)]

for each in mines:
    num1, num2 = each.split(", ")
    num1 = int(num1)
    num2 = int(num2)
    matrix[num1][num2] = "*"

# print("\n".join(''.join(map(str, x)) for x in matrix))

for i in range(n):
    for j in range(n):
        pos = matrix[i][j]

        if pos == "*":
            continue

        # right
        if j + 1 < n and matrix[i][j + 1] == "*":
            pos += 1
        # left
        if j - 1 >= 0 and matrix[i][j - 1] == "*":
            pos += 1
        # up
        if i + 1 < n and matrix[i + 1][j] == "*":
            pos += 1
        # down
        if i - 1 >= 0 and matrix[i - 1][j] == "*":
            pos += 1
        # right-up
        if i - 1 >= 0 and j + 1 < n and matrix[i - 1][j + 1] == "*":
            pos += 1
        # right-down
        if i + 1 < n and j + 1 < n and matrix[i + 1][j + 1] == "*":
            pos += 1
        # left-up
        if i - 1 >= 0 and j - 1 >= 0 and matrix[i - 1][j - 1] == "*":
            pos += 1
        # left-down
        if i + 1 < n and j - 1 >= 0 and matrix[i + 1][j - 1] == "*":
            pos += 1

        matrix[i][j] = pos

print("\n".join(' '.join(map(str, x)) for x in matrix))
