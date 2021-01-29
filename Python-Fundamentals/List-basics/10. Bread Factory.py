energy = 100
coins = 100
text = input().split("|")
counter = len(text)

for el in text:
    event, qty = el.split("-")
    qty = int(qty)

    if event == "rest":
        initial_energy = energy
        energy += qty
        if energy <= 100:
            print(f"You gained {qty} energy.")
        else:
            energy = 100
            print(f"You gained {100 - initial_energy} energy.")
        print(f"Current energy: {energy}.")

    elif event == "order":
        if energy - 30 >= 0:
            coins += qty
            energy -= 30
            print(f"You earned {qty} coins.")
        else:
            energy += 50
            print(f"You had to rest!")
    else:
        coins -= qty
        if coins > 0:
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            break
    counter -= 1

if counter == 0:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
