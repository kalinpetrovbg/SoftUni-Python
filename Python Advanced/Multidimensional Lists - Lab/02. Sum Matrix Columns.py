rows, cols = [int(x) for x in input().split(", ")]

matrix = []
matrix_sum = []

for x in range(rows):
    row = [int(x) for x in input().split(" ")]
    matrix.append(row)

for index_cols in range(cols):
    column_sum = 0
    for index_rows in range(rows):
        column_sum += matrix[index_rows][index_cols]
    matrix_sum.append(column_sum)

print(matrix_sum)


