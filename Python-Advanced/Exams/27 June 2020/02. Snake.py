n = int(input())
matrix = [list(input()) for _ in range(n)]
food = 0
holes = []
dead = False

while True:

    if dead == True:
        break

    command = input()

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == "S":

                if command == "right":
                    if j + 1 < n:
                        matrix[i][j] = "."
                        if matrix[i][j + 1] == "*":
                            food += 1
                        elif matrix[i][j + 1] == "B":
                            matrix[i][j] = "-"
                            matrix[i][j + 1] = "."

                            for y in range(n):
                                for z in range(n):
                                    if matrix[y][z] == "B":
                                        matrix[y][z] = "S"
                                        continue
                        matrix[i][j + 1] = "S"
                        break
                    else:
                        print(f"Game over!")
                        dead = True
                        break

                elif command == "left":
                    if j - 1 >= 0:
                        matrix[i][j] = "."
                        if matrix[i][j - 1] == "*":
                            food += 1
                        elif matrix[i][j - 1] == "B":
                            matrix[i][j] = "-"
                            matrix[i][j - 1] = "."

                            for y in range(n):
                                for z in range(n):
                                    if matrix[y][z] == "B":
                                        matrix[y][z] = "S"
                                        continue
                        matrix[i][j - 1] = "S"
                        break
                    else:
                        print(f"Game over!")
                        dead = True
                        break

                elif command == "down":
                    if i + 1 < n:
                        matrix[i][j] = "."
                        if matrix[i + 1][j] == "*":
                            food += 1
                        elif matrix[i + 1][j] == "B":
                            matrix[i][j] = "-"
                            matrix[i + 1][j] = "."

                            for y in range(n):
                                for z in range(n):
                                    if matrix[y][z] == "B":
                                        matrix[y][z] = "S"
                                        break
                        matrix[i + 1][j] = "S"
                        break
                    else:
                        print(f"Game over!")
                        dead = True
                        break

                elif command == "up":
                    if i - 1 <= 0:
                        matrix[i][j] = "."
                        if matrix[i - 1][j] == "*":
                            food += 1
                        elif matrix[i - 1][j] == "B":
                            matrix[i][j] = "-"
                            matrix[i - 1][j] = "."

                            for y in range(n):
                                for z in range(n):
                                    if matrix[y][z] == "B":
                                        matrix[y][z] = "S"
                                        continue
                        matrix[i - 1][j] = "S"
                        break
                    else:
                        print(f"Game over!")
                        dead = True
                        break


print("\n".join(''.join(map(str, x)) for x in matrix))