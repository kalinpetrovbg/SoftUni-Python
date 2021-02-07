people = {}
counter = {}
unliked = 0

text = input()

while text != "Stop":
    command, guest, meal = text.split("-")

    if command == "Like":
        if guest not in people:
            people[guest] = []
            people[guest].append(meal)
            counter[guest] = 1
        else:
            if meal not in people[guest]:
                people[guest].append(meal)
                counter[guest] += 1

    elif command == "Unlike":
        if guest not in people:
            print(f"{guest} is not at the party.")
        else:
            if meal not in people[guest]:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
            else:
                print(f"{guest} doesn't like the {meal}.")
                unliked += 1
                for l in people.values():
                    if meal in l: l.remove(meal)

    text = input()

for persons, num_meals in sorted(counter.items(), key=lambda x: (-x[1], x[0]), reverse=False):
    for names, meals in people.items():
        if persons == names:
            items = [str(el) for el in meals]
            food = ", ".join(items)
            print(f"{names}: {food}")

print(f"Unliked meals: {unliked}")