names = []
hidden = []

while True:
    text = input()
    if text != "End" and text != "Paid":
        name = text
        names.append(name)
    elif text == "Paid":
        print("\n".join(names))
        names.clear()

    elif text == "End":
        print(f"{len(names)} people remaining.")
        break
