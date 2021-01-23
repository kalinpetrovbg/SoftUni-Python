def is_valid(pos, size):                    # if hit inside or outside the board
    row = pos[0]
    col = pos[1]
    return 0 <= row < size and 0 <= col < size

def get_killed_knights(row, col, size, board):
    killed_knights = 0
    rows = [-2, -1, 1, 2, 2, 1, -1, -2]
    cols = [1, 2, 2, 1, -1, -2, -2, -1]
    for x in range(8):                                # 8 possible hits
        current_pos = [row + rows[x], col + cols[x]]
        if is_valid(current_pos, size) and board[current_pos[0][current_pos[1]]] == "K":
            killed_knights += 1
    return killed_knights

n = int(input())
matrix = [list(input()) for _ in range(n)]
most_kills = 0
total_kills = 0
to_kill = []

for i in range(len(matrix)):
    for j in range(n):
        if matrix[i][j] == "K":
            kills = get_killed_knights(i, j, n, matrix)
            if kills > most_kills:
                most_kills = kills
                to_kill = [i, j]

    if total_kills == 0:
        break

to_kill_row = to_kill[0]
to_kill_col = to_kill[1]
matrix[to_kill_row][to_kill_col] = "0"
total_kills += 1


print(total_kills)
for row in matrix:
    print(row)
