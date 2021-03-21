row, col = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(row)]
command = input().split()

while command[0] != "END":

    if command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
    else:
        old_row, old_col = int(command[1]), int(command[2])
        new_row, new_col = int(command[3]), int(command[4])

        if 0 <= old_row < row and 0 <= old_col < col and 0 <= new_row < row and 0 <= new_col < col:
            old_number = matrix[old_row][old_col]
            matrix[old_row][old_col] = matrix[new_row][new_col]
            matrix[new_row][new_col] = old_number
            print("\n".join(' '.join(map(str, x)) for x in matrix))
        else:
            print("Invalid input!")

    command = input().split()