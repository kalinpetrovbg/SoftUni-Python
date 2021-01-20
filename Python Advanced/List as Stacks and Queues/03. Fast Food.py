from collections import deque

food_capacity = int(input())
q = deque([int(x) for x in input().split()])

print(max(q))

while len(q) > 0:
    current = q[0]
    if current <= food_capacity:
        q.popleft()
        food_capacity -= current
    else:
        break

result = [str(x) for x in q]

if len(q) == 0:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(result)}")
