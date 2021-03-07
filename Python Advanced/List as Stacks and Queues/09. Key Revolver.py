from collections import deque

price = int(input())
barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence = int(input())
shots = 0

while locks and bullets:
    current_bullet = bullets.pop()
    current_lock = locks.popleft()
    shots += 1

    if current_bullet > current_lock:
        print("Ping!")
        locks.appendleft(current_lock)
    else:
        print("Bang!")

    if shots % barrel == 0 and bullets:
        print("Reloading!")
        c_barrel = barrel

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${intelligence - (shots * price)}")
elif not bullets:
    print(f"Couldn't get through. Locks left: {len(locks)}")
