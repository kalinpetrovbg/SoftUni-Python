row, col = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(row)]
counter = 0

for i in range(row - 1):
    for j in range(col - 1):
        if matrix[i][j] == matrix[i][j+1] == matrix[i+1][j] == matrix[i+1][j+1]:
            counter += 1

print(counter)