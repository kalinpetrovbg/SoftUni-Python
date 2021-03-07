matrix = [[x for x in input().split()] for _ in range(8)]

pos = []
queens = []
counter = 0

for i in range(8):
    for j in range(8):
        if matrix[i][j] == "K":
            pos.extend((i, j))


print(pos)

for i in range(8):
    for j in range(8):
        if matrix[i][j] == "Q":
            q = [i, j]

            # horizontal right moves
            for index in range(1, 8):
                if j + index == 8:
                    break
                current = matrix[i][j + index]
                if current == "K":
                    counter += 1
                    print(f"{[i, j]}")
                if current == "Q":
                    break

            # horizontal left moves
            for index in range(1, 8):
                if j - index < 0:
                    break
                current = matrix[i][j - index]
                if current == "K":
                    counter += 1
                    print(f"{[i, j]}")
                if current == "Q":
                    break

            # diagonal right down moves
            for index in range(1, 8):
                if i + index == 8 or j + index == 8:
                    break
                current = matrix[i + index][j + index]
                if current == "K":
                    counter += 1
                    print(f"{[i, j]}")
                if current == "Q":
                    break

            # diagonal left up moves
            for index in range(1, 8):
                if i - index < 0 or j - index < 0:
                    break
                current = matrix[i - index][j - index]
                if current == "K":
                    counter += 1
                    print(f"{[i, j]}")
                if current == "Q":
                    break

            # vertical down moves
            for index in range(1, 8):
                if i + index == 8:
                    break
                current = matrix[i + index][j]
                if current == "K":
                    counter += 1
                    print(f"{[i, j]}")
                if current == "Q":
                    break

            # vertical up moves
            for index in range(1, 8):
                if i - index < 0:
                    break
                current = matrix[i - index][j]
                if current == "K":
                    counter += 1
                    print(f"{[i, j]}")
                if current == "Q":
                    break


            # diagonal right up moves
            for index in range(1, 8):
                if i - index < 0 or j + index == 8:
                    break
                current = matrix[i - index][j + index]
                if current == "K":
                    counter += 1
                    print(f"{[i, j]}")
                if current == "Q":
                    break

            # diagonal left down moves
            for index in range(1, 8):
                if i + index == 8 or j - index < 0:
                    break
                current = matrix[i + index][j - index]
                if current == "K":
                    counter += 1
                    print(f"{[i, j]}")
                if current == "Q":
                    break



if counter != 0:
    pass
else:
    print("The king is safe!")

