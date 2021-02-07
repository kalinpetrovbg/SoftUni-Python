items = input().split("!")
command = input()

while command != "Go Shopping!":

    if "Urgent" in command:
        action, item = command.split(" ")
        if item not in items:
            items.insert(0, item)

    elif "Unnecessary" in command:
        action, item = command.split(" ")
        if item in items:
            items.remove(item)

    elif "Rearrange" in command:
        action, item = command.split(" ")
        if item in items:
            items.remove(item)
            items.append(item)

    elif "Correct" in command:
        action, old, new = command.split(" ")
        if old in items:
            items.insert(items.index(old), new)
            items.remove(old)

    command = input()

print(", ".join(items))