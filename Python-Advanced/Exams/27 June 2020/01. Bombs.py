bomb_effect = [int(x) for x in input().split(", ")]
bomb_casing = [int(x) for x in input().split(", ")]
bombs = {}
total_bombs = 0
mapper = {
    40 : "Datura Bombs",
    60 : "Cherry Bombs",
    120 : "Smoke Decoy Bombs",
}

while bomb_casing:

    effect = bomb_effect[0]
    casing = bomb_casing[-1]
    current_sum = effect + casing
    if current_sum in mapper:
        bomb_effect.pop(0)
        bomb_casing.pop(-1)
        total_bombs += 1
        if mapper[current_sum] not in bombs:
            bombs[mapper[current_sum]] = 0
        bombs[mapper[current_sum]] += 1
    else:
        bomb_casing[-1] -= 5


print(bombs)