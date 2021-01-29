n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

command = input()
while command != "END":
    method, row, col, value = command.split()
    if n - 1 < int(row) or int(row) < 0 or n - 1 < int(col) or int(col) < 0:
        print("Invalid coordinates")
        command = input()
        continue
    elif method == "Add":
        matrix[int(row)][int(col)] += int(value)
    elif method == "Subtract":
        matrix[int(row)][int(col)] -= int(value)
    command = input()

print('\n'.join(" ".join(map(str, x)) for x in matrix))