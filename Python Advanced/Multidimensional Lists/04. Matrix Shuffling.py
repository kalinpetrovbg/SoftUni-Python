rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

command = input().split()

while command[0] != "END":

    if command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
    else:
        a, b, c, d = [int(x) for x in command[1:]]
        if a > rows - 1 or c > rows - 1 or b > cols - 1 or d > cols - 1:
            print("Invalid input!")
        else:
            temp = matrix[int(a)][int(b)]
            matrix[int(a)][int(b)] = matrix[int(c)][int(d)]
            matrix[int(c)][int(d)] = temp

            print("\n".join(' '.join(map(str, x)) for x in matrix))

    command = input().split()