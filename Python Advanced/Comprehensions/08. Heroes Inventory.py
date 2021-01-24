names = input().split(", ")

command = input()
result = {}
cost = {}

while command != "End":
    name, item, price = command.split("-")
    price = int(price)
    if name not in result:
        result[name] = []
        cost[name] = []
        if item not in result[name]:
            result[name].append(item)
            cost[name].append(price)
    else:
        if item not in result[name]:
            result[name].append(item)
            cost[name].append(price)

    command = input()

for name, items in result.items():
    for person, total in cost.items():
        if name == person:
            print(f"{name} -> Items: {len(result[name])}, Cost: {sum(total)}")

