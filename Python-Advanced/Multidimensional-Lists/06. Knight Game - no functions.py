n = int(input())
matrix = [[x for x in list(input())] for _ in range(n)]
removed = 0
hit_row = (-2, -2, +2, +2, -1, -1, +1, +1)
hit_col = (-1, +1, -1, +1, -2, +2, +2, -2)

while True:
    best_killer = 0
    monster = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == "K":
                kills = 0
                for x in range(8):
                    if 0 <= i + hit_row[x] < n and 0 <= j + hit_col[x] < n:
                        if matrix[i + hit_row[x]][j + hit_col[x]] == "K":
                            kills += 1
                if best_killer < kills:
                    monster = [i, j]
                    best_killer = kills
    if monster:
        matrix[monster[0]][monster[1]] = 0
        removed += 1
    else:
        break

print(removed)