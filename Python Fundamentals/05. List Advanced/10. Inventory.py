items = input().split(", ")
command = input()

while not command == "Craft!":
    action, item = command.split(" - ")

    if action == "Collect":
        if item not in items:
            items.append(item)

    elif action == "Drop":
        if item in items:
            items.remove(item)

    elif action == "Combine Items":
        old, new = item.split(":")
        if old in items:
            place = items.index(old)
            items.insert(place + 1, new)

    elif action == "Renew":
        if item in items:
            items.remove(item)
            items.append(item)

    command = input()

print(", ".join(items))