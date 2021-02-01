n = int(input())
matrix = [[int(x) for x in input().split(" ")] for _ in range(n)]
bombs = input().split(" ")
num_bombs = len(bombs)
print(num_bombs)
bomb1 = [int(x) for x in bombs[0].split(",")]
bomb2 = [int(x) for x in bombs[1].split(",")]
bomb3 = [int(x) for x in bombs[2].split(",")]

hit_row = (-1,-1, -1, 0, 0, 0, +1,+1, +1)
hit_col = (-1, 0, +1,-1, 0,+1, -1, 0, +1)

for i in range(n):
    for j in range(n):
        if i == bomb1[0] and j == bomb1[1] and matrix[i][j] > 0:
            current1 = matrix[i][j]
            for index in range(9):
                hit_r = i + hit_row[index]
                hit_c = j + hit_col[index]
                if 0 <= hit_r < n and 0 <= hit_c < n:
                    if matrix[i + hit_row[index]][j + hit_col[index]] > 0:
                        matrix[i + hit_row[index]][j + hit_col[index]] -= current1
                        matrix[i][j] = 0

for i in range(n):
    for j in range(n):
        if i == bomb2[0] and j == bomb2[1] and matrix[i][j] > 0:
            current2 = matrix[i][j]
            for index in range(9):
                hit_r = i + hit_row[index]
                hit_c = j + hit_col[index]
                if 0 <= hit_r < n and 0 <= hit_c < n:
                    if matrix[i + hit_row[index]][j + hit_col[index]] > 0:
                        matrix[i + hit_row[index]][j + hit_col[index]] -= current2
                        matrix[i][j] = 0

for i in range(n):
    for j in range(n):
        if i == bomb3[0] and j == bomb3[1] and matrix[i][j] > 0:
            current3 = matrix[i][j]
            for index in range(9):
                hit_r = i + hit_row[index]
                hit_c = j + hit_col[index]
                if 0 <= hit_r < n and 0 <= hit_c < n:
                    if matrix[i + hit_row[index]][j + hit_col[index]] > 0:
                        matrix[i + hit_row[index]][j + hit_col[index]] -= current3
                        matrix[i][j] = 0

total = []
for el in matrix:
    for each in el:
        if each > 0:
            total.append(each)

print(f"Alive cells: {len(total)}")
print(f"Sum: {sum(total)}")
print("\n".join(' '.join(map(str, x)) for x in matrix))