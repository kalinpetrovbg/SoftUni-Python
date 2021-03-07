rows, cols = [int(x) for x in input().split()]
matrix = []
alpha = "abcdefghijklmnopqrstuvwxyz"

for i in range(rows):
    matrix.append([])
    for j in range(cols):
        matrix[i].append(alpha[i] + alpha[j + i] + alpha[i])

print("\n".join(' '.join(map(str, x)) for x in matrix))