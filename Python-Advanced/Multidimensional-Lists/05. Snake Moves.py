from collections import deque

row, col = [int(x) for x in input().split()]
word = deque(list(input()))

matrix = []

for i in range(row):
    matrix.append([])
    for j in range(col):
        matrix[i].append("")

for i in range(row):
    for j in range(col):
        current_col = j
        current_char = word.popleft()
        if i % 2 != 0:
            current_col = col - 1 - j
        matrix[i][current_col] = current_char
        word.append(current_char)

for row in matrix:
    print("".join(str(x) for x in row))