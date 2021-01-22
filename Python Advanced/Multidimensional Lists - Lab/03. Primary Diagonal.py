n = int(input())
matrix = []
for _ in range(n):
    line = [int(x) for x in input().split()]
    matrix.append(line)

diagonal_sum = 0

for i in range(len(matrix)):
    diagonal_sum += matrix[i][i]

print(diagonal_sum)