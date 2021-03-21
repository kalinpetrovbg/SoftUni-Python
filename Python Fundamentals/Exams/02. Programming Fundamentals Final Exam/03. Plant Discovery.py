n = int(input())
plants = {}
new_plants = {}

for _ in range(n):
    name, rare = input().split("<->")
    plants[name] = [int(rare)]

data = input()

while data != "Exhibition":
    data = data.replace(" - ", ": ")
    data = data.split(": ")

    if data[0] == "Rate":
        plant, rating = data[1:]
        if plant in plants and int(rating) > 0:
            plants[plant].append(float(rating))
        else:
            print(f"error")

    elif data[0] == "Update":
        plant, rarity = data[1:]
        if plant in plants and int(rarity) > 0:
            plants[plant][0] = int(rarity)
        else:
            print(f"error")

    elif data[0] == "Reset":
        plant = data[1]
        if plant in plants:
            del plants[plant][1:]
        else:
            print(f"error")

    else:
        print(f"error")

    data = input()

for plant, stats in plants.items():
    if len(stats) > 1:
        rating = sum(stats[1:]) / (len(stats) - 1)
        new_plants[plant] = [stats[0], rating]
    else:
        new_plants[plant] = [stats[0], 0.00]

print("Plants for the exhibition:")
for plant, stats in sorted(new_plants.items(), key=lambda x: (-x[1][0], -x[1][1])):
    print(f"- {plant}; Rarity: {stats[0]}; Rating: {stats[1]:.2f}")