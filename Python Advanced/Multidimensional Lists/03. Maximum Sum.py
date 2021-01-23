from itertools import chain

rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
maximum_sum = -999999
biggest_matrix = []

for i in range(rows - 2):
    for j in range(cols - 2):
        sub_matrix = []
        for y in range(i, i + 3):
            add_value = []
            for z in range(j, j + 3):
                add_value.append(matrix[y][z])
            sub_matrix.append(add_value)

        sum_res = sum(chain(*sub_matrix))
        if sum_res > maximum_sum:
            maximum_sum = sum_res
            biggest_matrix = sub_matrix

print(f"Sum = {maximum_sum}")
print("\n".join(' '.join(map(str, x)) for x in biggest_matrix))