rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)]

counter = 0

for i in range(len(matrix) - 1):
    for j in range(cols - 1):
        current = matrix[i][j]
        if current == matrix[i][j + 1] and matrix[i + 1][j] == matrix[i + 1][j + 1] and matrix[i + 1][j] == current:
            counter += 1

print(counter)
