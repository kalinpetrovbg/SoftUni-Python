qty = int(input())
days = int(input())
budget = 0
spirit = 0
new_qty = 0
day_c = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        qty += 2
    if day % 2 == 0:
        budget += qty * 2
        spirit += 5
    if day % 3 == 0:
        budget += qty * 8
        spirit += 13
    if day % 5 == 0:
        budget += qty * 15
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        budget += 23
if days % 10 == 0:
    spirit -= 30


print(f"Total cost: {budget}")
print(f"Total spirit: {spirit}")