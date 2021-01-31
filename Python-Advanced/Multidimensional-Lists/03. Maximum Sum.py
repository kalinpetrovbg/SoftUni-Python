row, col = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(row)]
total = 0
maximum = -999999

for i in range(row - 2):
    for j in range(col - 2):
        line1 = [matrix[i][j], matrix[i][j+1], matrix[i][j+2]]
        line2 = [matrix[i+1][j], matrix[i+1][j+1], matrix[i+1][j+2]]
        line3 = [matrix[i+2][j], matrix[i+2][j+1], matrix[i+2][j+2]]
        total = sum(line1) + sum(line2) + sum(line3)

        if total > maximum:
            maximum = total
            best_line1 = line1
            best_line2 = line2
            best_line3 = line3

print(f"Sum = {maximum}")
print(" ".join(map(str, best_line1)))
print(" ".join(map(str, best_line2)))
print(" ".join(map(str, best_line3)))