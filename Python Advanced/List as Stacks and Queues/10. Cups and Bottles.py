from collections import deque

cups_capacity = deque([int(x) for x in input().split()])
bottles_with_water = [int(x) for x in input().split()]
filled_cups = 0
wasted_water = []
not_empty = False

while cups_capacity:
    current_water = bottles_with_water[-1]
    if not_empty == False:
        current_cup = cups_capacity[0]

    if current_water >= current_cup:
        cups_capacity.popleft()
        bottles_with_water.pop()
        wasted_water.append(current_water - current_cup)
        not_empty = False

    else:
        current_cup -= current_water
        bottles_with_water.pop()
        if current_cup > 0:
            not_empty = True
        else:
            is_empty = False

    if not bottles_with_water:
        break

if bottles_with_water:
    print(f"Bottles: {' '.join(str(x) for x in bottles_with_water)}")
else:
    print(f"Cups: {' '.join(str(x) for x in cups_capacity)}")
print(f"Wasted litters of water: {sum(wasted_water)}")

