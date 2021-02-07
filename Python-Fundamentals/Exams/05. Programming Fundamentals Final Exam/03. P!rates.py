commands = input()
target = {}
while commands != "Sail":
    city, population, gold = commands.split("||")
    if city not in target:
        target[city] = [int(population), int(gold)]
    else:
        target[city][0] += int(population)
        target[city][1] += int(gold)
    commands = input()

action = input()

while action != "End":
    data = action.split("=>")

    if data[0] == "Plunder":
        town, people, stolen = data[1:]
        people = int(people)
        stolen = int(stolen)
        target[town][0] -= people
        target[town][1] -= stolen
        print(f"{town} plundered! {stolen} gold stolen, {people} citizens killed.")
        if target[town][0] <= 0 or target[town][1] <= 0:
            del target[town]
            print(f"{town} has been wiped off the map!")

    elif data[0] == "Prosper":
        town, grow = data[1:]
        grow = int(grow)
        if grow < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            target[town][1] += grow
            print(f"{grow} gold added to the city treasury. {town} now has {target[town][1]} gold.")

    action = input()

print(f"Ahoy, Captain! There are {len(target)} wealthy settlements to go to:")

for city, stats in sorted(target.items(), key=lambda x: (-x[1][1], x[0])):
    print(f"{city} -> Population: {stats[0]} citizens, Gold: {stats[1]} kg")

