n = int(input())
matrix = [[int(x) for x in input().split(" ")] for _ in range(n)]
attacks = [x for x in input().split(" ")]
destroyed = 0

for each in attacks:
    row, col = each.split("-")
    row = int(row)
    col = int(col)
    if matrix[row][col] > 0:
        matrix[row][col] -= 1
        if matrix[row][col] == 0:
            destroyed += 1

print(destroyed)