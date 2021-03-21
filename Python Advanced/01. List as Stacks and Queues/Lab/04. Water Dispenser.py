from collections import deque
queue = deque()
capacity = int(input())
command = input()

while command != "Start":
    queue.append(command)
    command = input()

text = input()
while text != "End":
    message = text.split()
    if len(message) == 1:
        liters = int(message[0])
        if liters <= capacity:
            person = queue.popleft()
            capacity -= liters
            print(f"{person} got water")
        else:
            person = deque.popleft(queue)
            print(f"{person} must wait")

    if len(message) == 2:
        refill = int(message[1])
        capacity += refill

    text = input()

print(f"{capacity} liters left")