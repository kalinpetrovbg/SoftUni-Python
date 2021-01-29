from collections import deque

names = input().split()
step = int(input())

counter = 0

queue = deque(names)

while len(queue) > 1:
    for _ in range(step - 1):
        queue.append(queue.popleft())
    print(f"Removed {queue.popleft()}")

print(f"Last is {queue[0]}")
