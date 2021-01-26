names = input().split(", ")
heroes = {name: {} for name in names}
command = input()

while command != "End":
    name, item, qty = command.split("-")
    qty = int(qty)
    if not heroes[name]:
        heroes[name] = []
    if item not in heroes[name]:
        heroes[name].append(item)
        heroes[name].append(qty)
    command = input()

for key, value in heroes.items():
    total = [x for x in value if str(x).isdigit()]
    print(f"{key} -> Items: {len(value) // 2}, Cost: {sum(total)} ")