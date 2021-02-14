effects = [int(x) for x in input().split(", ") if int(x) > 0]
powers = [int(x) for x in input().split(", ") if int(x) > 0]
fire = {"Palm Fireworks": 0, "Willow Fireworks": 0, "Crossette Fireworks": 0}
fires = False

while effects and powers:

    if effects[0] <= 0:
        effects.pop(0)
    if powers[-1] <= 0:
        powers.pop(-1)

    if effects and powers:
        effect = effects.pop(0)
        power = powers.pop(-1)
        total = effect + power
    else:
        break

    if total % 3 == 0 and total % 5 != 0:
        fire["Palm Fireworks"] += 1
    elif total % 5 == 0 and total % 3 != 0:
        fire["Willow Fireworks"] += 1
    elif total % 3 == 0 and total % 5 == 0:
        fire["Crossette Fireworks"] += 1
    else:
        effect -= 1
        effects.append(effect)
        powers.append(power)

    if fire["Palm Fireworks"] >= 3 and fire["Willow Fireworks"] >= 3 and fire["Crossette Fireworks"] >= 3:
        print("Congrats! You made the perfect firework show!")
        fires = True
        break

if not fires:
    print("Sorry. You can’t make the perfect firework show.")

if effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in effects)}")
if powers:
    print(f"Explosive Power left: {', '.join(str(x) for x in powers)}")

for key, value in fire.items():
    print(f"{key}: {value}")
