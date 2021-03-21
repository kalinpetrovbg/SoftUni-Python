rooms = input().split("|")
health = 100
bitcoins = 0
room = 0

for each in rooms:
    command, number = each.split(" ")
    number = int(number)
    room += 1

    if command == "potion":
        if health + number >= 100:
            print(f"You healed for {100 - health} hp.")
            health = 100
        else:
            health += number
            print(f"You healed for {number} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room}")
            break

if health > 0:
    print(f"You\'ve made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")

