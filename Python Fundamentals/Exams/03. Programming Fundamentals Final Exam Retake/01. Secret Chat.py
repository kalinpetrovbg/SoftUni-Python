message = input()
command = input()
errors = False

while command != "Reveal":
    data = command.split(":|:")

    if data[0] == "InsertSpace":
        index = int(data[1])
        message = message[:index] + " " + message[index:]

    elif data[0] == "Reverse":
        substring = data[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            substring = substring[::-1]
            message += substring
        else:
            print(f"error")
            errors = True

    elif data[0] == "ChangeAll":
        substring = data[1]
        n = message.count(substring)
        message = message.replace(substring, data[2], n)

    command = input()

    if not errors:
        print(message)
    errors = False

print(f"You have a new text message: {message}")
