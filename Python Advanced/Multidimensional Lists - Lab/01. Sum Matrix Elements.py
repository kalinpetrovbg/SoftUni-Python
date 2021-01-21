rows, cols = [int(x) for x in input().split(", ")]

matrix = []
for x in range(rows):
    row = [int(x) for x in input().split(",")]
    matrix.append(row)

matrix_sum = 0

for r in range(len(matrix)):
    row = matrix[r]
    for c in range(len(row)):
        matrix_sum += row[c]

print(matrix_sum)
print(matrix)