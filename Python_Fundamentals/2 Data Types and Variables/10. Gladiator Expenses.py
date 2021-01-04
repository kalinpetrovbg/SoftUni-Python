lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

shield = 0

money = 0

for x in range(1, lost_fights + 1):
    if x % 2 == 0:
        money += helmet_price
    if x % 3 == 0:
        money += sword_price
        if x % 2 == 0:
            money += shield_price
            shield += 1
    if shield == 2:
        money += armor_price
        shield = 0
print(f"Gladiator expenses: {money:.2f} aureus")