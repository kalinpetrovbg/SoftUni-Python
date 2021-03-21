from collections import deque

total = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

if sum(orders) <= total:
    print("Orders complete")
else:
    for order in range(len(orders)):
        if total >= orders[0]:
            completed = orders.popleft()
            total -= completed
        else:
            print(f"Orders left: {' '.join(map(str, orders))}")
            break