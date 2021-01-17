from collections import deque

bullet_price = int(input())
size_of_barrel = int(input())
bullets = [int(x) for x in input().split()]
lockers = deque([int(y) for y in input().split()])
intelligence = int(input())
total_shots = 0

while bullets:
    if lockers:
        bullet = bullets.pop()
        total_shots += 1

        if bullet <= lockers[0]:
            lockers.popleft()
            print("Bang!")
        else:
            print("Ping!")

        if bullets:
            if total_shots % size_of_barrel == 0:
                print("Reloading!")
    else:
        break

if not lockers:
    bullet_cost = total_shots * bullet_price
    print(f"{len(bullets)} bullets left. Earned ${intelligence - bullet_cost}")
else:
    print(f"Couldn't get through. Locks left: {len(lockers)}")
