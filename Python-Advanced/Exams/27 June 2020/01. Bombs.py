bomb_effect = [int(x) for x in input().split(", ")]
bomb_casing = [int(x) for x in input().split(", ")]
bombs = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}

mapper = {
    40: "Datura Bombs",
    60: "Cherry Bombs",
    120: "Smoke Decoy Bombs",
}

while bomb_effect and bomb_casing:
    effect = bomb_effect[0]
    casing = bomb_casing[-1]
    current_sum = effect + casing

    if current_sum in mapper:
        bomb_effect.pop(0)
        bomb_casing.pop(-1)
        bombs[mapper[current_sum]] += 1

    else:
        bomb_casing[-1] -= 5

    if bombs["Datura Bombs"] >= 3 and bombs["Cherry Bombs"] >= 3 and bombs["Smoke Decoy Bombs"] >= 3:
        break

if bombs["Datura Bombs"] >= 3 and bombs["Cherry Bombs"] >= 3 and bombs["Smoke Decoy Bombs"] >= 3:
    print(f"Bene! You have successfully filled the bomb pouch!")
else:
    print(f"You don't have enough materials to fill the bomb pouch.")

if not bomb_effect:
    print(f"Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effect))}")

if not bomb_casing:
    print(f"Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join(map(str, bomb_casing))}")

for name, qty in sorted(bombs.items(), key=lambda x: x[0]):
    print(f"{name}: {qty}")
