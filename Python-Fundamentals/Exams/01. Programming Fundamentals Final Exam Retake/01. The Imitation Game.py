message = input()
text = input()

while text != "Decode":
    command = text.split("|")
    if command[0] == "Move":
        index = int(command[1])
        message = message[index:] + message[:index]
    elif command[0] == "Insert":
        index = int(command[1])
        ending = message[index:]
        message = message[:index] + command[2] + ending
    elif command[0] == "ChangeAll":
        temp = str.maketrans(command[1], command[2])
        message = message.translate(temp)
    text = input()

print(f"The decrypted message is: {message}")