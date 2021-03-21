from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]
wasted = 0

while bottles:
    c_bottle = bottles.pop()
    c_cup = cups.popleft()

    if c_bottle >= c_cup:
        wasted += (c_bottle - c_cup)
    else:
        c_cup -= c_bottle
        cups.appendleft(c_cup)

    if not cups:
        print(f'Bottles: {" ".join(map(str, bottles))}')
        break
    if not bottles:
        print(f'Cups: {" ".join(map(str, cups))}')
        break

print(f"Wasted litters of water: {wasted}")
