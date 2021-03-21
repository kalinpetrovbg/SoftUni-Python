all_cards = input().split(":")
command = input()
new_cards = []

while not command == "Ready":

    if "Add" in command:
        add, comm = command.split()
        if comm not in all_cards:
            print("Card not found.")
        else:
            new_cards.append(comm)

    elif "Insert" in command:
        add, card, index = command.split()
        index = int(index)
        if card not in all_cards:
            print("Error!")
        else:
            new_cards.insert(index, card)

    elif "Swap" in command:
        swap, card1, card2 = command.split()
        if card1 in new_cards:
            card1_index = new_cards.index(card1)
        if card2 in new_cards:
            card2_index = new_cards.index(card2)

        new_cards[card1_index], new_cards[card2_index] = new_cards[card2_index], new_cards[card1_index]

    elif "Remove" in command:
        rem, comm = command.split()
        if comm not in new_cards:
            print("Card not found.")
        else:
            new_cards.remove(comm)

    elif "Shuffle" in command:
        new_cards.reverse()

    command = input()

new_cards_str = [str(el) for el in new_cards]
print(" ".join(new_cards_str))