energy = int(input())
battles = 0

while True:
    command = input()

    if command == "End of battle":
        print(f"Won battles: {battles}. Energy left: {energy}")
        break
    else:
        distance = int(command)
        if energy - distance >= 0:
            energy -= distance
            battles += 1
            if battles % 3 == 0:
                energy += battles
        else:
            print(f"Not enough energy! Game ends with {battles} won battles and {energy} energy")
            break

