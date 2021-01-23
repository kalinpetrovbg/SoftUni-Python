from collections import deque

row, col = [int(x) for x in input().split()]
word = deque(list(input()))

for i in range(row):
    line = ""
    for _ in range(col):
        piece = word.popleft()
        line += piece
        word.append(piece)
    if i % 2 == 0:
        print(line)
    else:
        print(line[::-1])