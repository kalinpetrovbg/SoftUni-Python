n = int(input())
matrix = [list(input()) for _ in range(n)]

best_knight_killer = False
any_kills = True
kills = 0
most_kills = 0
hits = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
removed_knights = 0

while any_kills:
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "K":
                for i in range(8):
                    new_row = row + hits[i][0]
                    new_col = col + hits[i][1]
                    if new_row < 0 or new_col < 0 or new_row > n - 1 or new_col > n - 1:
                        continue
                    else:
                        new_position = matrix[row + hits[i][0]][col + hits[i][1]]
                        if new_position == "K":
                            kills += 1
                            any_kills = True

                if kills > most_kills:
                    most_kills = kills
                    best_knight_killer = matrix[row][col]
                    update = row, col
                kills = 0

    if best_knight_killer:
        best_knight_killer = 0
        matrix[update[0]][update[1]] = 0
        if most_kills != 0:
            removed_knights += 1
    else:
        any_kills = False
        break

print("-----------")
print("\n".join(''.join(map(str, x)) for x in matrix))

print(removed_knights)
