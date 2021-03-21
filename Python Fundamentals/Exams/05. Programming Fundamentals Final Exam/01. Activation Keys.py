text = input()
command = input()

while command != "Generate":
    data = command.split(">>>")

    if data[0] == "Contains":
        substring = data[1]
        if substring in text:
            print(f"{text} contains {substring}")
        else:
            print("Substring not found!")

    elif data[0] == "Flip":
        start = int(data[2])
        end = int(data[3])
        if data[1] == "Upper":
            text = text[:start] + text[start:end].upper() + text[end:]
        else:
            text = text[:start] + text[start:end].lower() + text[end:]
        print(text)

    elif data[0] == "Slice":
        start = int(data[1])
        end = int(data[2])
        text = text[:start] + text[end:]
        print(text)

    command = input()

print(f"Your activation key is: {text}")
