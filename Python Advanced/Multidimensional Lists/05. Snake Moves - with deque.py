from collections import deque

rows, cols = list(map(int, input().split()))
word = input()
deq = deque()

for index in range(rows):
    line = ""
    for _ in range(cols):
        if not deq:
            deq = deque(word)
        line += deq.popleft()
    if index % 2 == 0:
        print(line)
    else:
        print(line[::-1])
