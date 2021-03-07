text = input()
phonebook = {}

while not text.isdigit():

    if text.isdigit():
        break
    name, phone = text.split("-")
    if name not in phonebook:
        phonebook[name] = phone
    text = input()

num = int(text)

for _ in range(num):
    check = input()

    if check in phonebook:
        print(f"{check} -> {phonebook[check]}")
    else:
        print(f"Contact {check} does not exist.")
