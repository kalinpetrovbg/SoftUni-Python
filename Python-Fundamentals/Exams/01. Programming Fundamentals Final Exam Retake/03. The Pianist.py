n = int(input())
songs = {}

for _ in range(n):
    piece, composer, key = input().split("|")
    songs[piece] = [composer, key]

command = input()

while command != "Stop":
    text = command.split("|")
    action, piece = text[:2]

    if action == "Add":
        if piece not in songs:
            songs[piece] = [text[2], text[3]]
            print(f"{piece} by {text[2]} in {text[3]} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    if action == "Remove":
        if piece in songs:
            songs.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    if action == "ChangeKey":
        if piece not in songs:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            songs[piece][1] = text[2]
            print(f"Changed the key of {piece} to {text[2]}!")

    command = input()

for piece, composer in sorted(songs.items(), key=lambda x: (x[0], x[1])):
    print(f"{piece} -> Composer: {composer[0]}, Key: {composer[1]}")