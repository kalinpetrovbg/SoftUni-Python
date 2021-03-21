password = input()
command = input()

while command != "Done":
    data = command.split()

    if data[0] == "TakeOdd":
        password = [password[x] for x in range(len(password)) if x % 2 != 0]
        password = "".join(password)
        print(password)

    elif data[0] == "Cut":
        index = int(data[1])
        length = index + int(data[2])
        password = password[:index] + password[length:]
        print(password)

    elif data[0] == "Substitute":
        old = data[1]
        new = data[2]
        if old in password:
            password = password.replace(old, new)
            print(password)
        else:
            print(f"Nothing to replace!")

    command = input()

print(f"Your password is: {password}")