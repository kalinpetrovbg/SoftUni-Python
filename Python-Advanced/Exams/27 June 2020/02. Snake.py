n = int(input())
matrix = [list(input()) for _ in range(n)]
food = 0
dead = False
clear = False
found_b = False

while food != 10:

    if dead:
        break

    command = input()
    move = False

    for i in range(n):
        if move:
            break
        if dead:
            break
        for j in range(n):

            while found_b:
                for y in range(n):
                    for z in range(n):
                        if matrix[y][z] == "B":
                            matrix[y][z] = "S"
                            found_b = False
                            move = True
                            continue
            if move:
                break
            move = False

            if matrix[i][j] == "S":
                matrix[i][j] = "."

                if command == "right":
                    if j + 1 < n:
                        if matrix[i][j + 1] == "*":
                            food += 1
                        elif matrix[i][j + 1] == "B":
                            matrix[i][j + 1] = "."
                            found_b = True
                            break
                        matrix[i][j + 1] = "S"
                        move = True
                        break

                elif command == "left":
                    if j - 1 >= 0:
                        if matrix[i][j - 1] == "*":
                            food += 1
                        elif matrix[i][j - 1] == "B":
                            matrix[i][j - 1] = "."
                            found_b = True
                            break
                        matrix[i][j - 1] = "S"
                        move = True
                        break

                elif command == "down":
                    if i + 1 < n:
                        if matrix[i + 1][j] == "*":
                            food += 1
                        elif matrix[i + 1][j] == "B":
                            matrix[i + 1][j] = "."
                            found_b = True
                            break
                        matrix[i + 1][j] = "S"
                        move = True
                        break

                elif command == "up":
                    if i - 1 >= 0:
                        if matrix[i - 1][j] == "*":
                            food += 1
                        elif matrix[i - 1][j] == "B":
                            matrix[i - 1][j] = "."
                            found_b = True
                            break
                        matrix[i - 1][j] = "S"
                        move = True
                        break

                if not move:
                    print(f"Game over!")
                    dead = True
                    break

                if food == 10:
                    move = True
                    break

if food == 10:
    print("You won! You fed the snake.")
print(f"Food eaten: {food}")
print("\n".join(''.join(map(str, x)) for x in matrix))
