n = int(input())
heroes = {}
for _ in range(n):
    name, health, mana = input().split()
    heroes[name] = [int(health), int(mana)]
command = input()

while command != "End":
    data = command.split(" - ")

    if data[0] == "CastSpell":
        name, mp, spell = data[1:]
        mp = int(mp)
        if mp <= heroes[name][1]:
            heroes[name][1] -= mp
            print(f"{name} has successfully cast {spell} and now has {heroes[name][1]} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell}!")

    elif data[0] == "TakeDamage":
        name, damage, attacker = data[1:]
        damage = int(damage)
        heroes[name][0] -= damage
        if heroes[name][0] <= 0:
            print(f"{name} has been killed by {attacker}!")
            del heroes[name]
        else:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name][0]} HP left!")

    elif data[0] == "Recharge":
        name, amount = data[1:]
        amount = int(amount)
        if heroes[name][1] + amount > 200:
            amount = 200 - heroes[name][1]
            heroes[name][1] = 200
        else:
            heroes[name][1] += amount
        print(f"{name} recharged for {amount} MP!")

    elif data[0] == "Heal":
        name, amount = data[1:]
        amount = int(amount)
        if heroes[name][0] + amount > 100:
            amount = 100 - heroes[name][0]
            heroes[name][0] = 100
        else:
            heroes[name][0] += amount
        print(f"{name} healed for {amount} HP!")

    command = input()

for hero, stats in sorted(heroes.items(), key=lambda x: (-x[1][0], x[0])):
    print(f"{hero}")
    print(f"  HP: {stats[0]}")
    print(f"  MP: {stats[1]}")