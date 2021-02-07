text = input()

line = input()

while line != "Done":
    command = line.split()

    if command[0] == "Change":
        old_letter = command[1]
        new_letter = command[2]
        text = text.replace(old_letter, new_letter)
        print(text)

    elif command[0] == "Includes":
        word_to_check = command[1]
        if word_to_check in text:
            print("True")
        else:
            print("False")

    elif command[0] == "End":
        if_ends_with = command[1]
        count_ends = len(if_ends_with)
        last_from_text = text[-count_ends:]
        # print(f"Ends with {last_from_text}")   за дебъгинг
        if if_ends_with == last_from_text:
            print("True")
        else:
            print("False")

    elif command[0] == "Uppercase":
        text = text.upper()
        print(text)

    elif command[0] == "FindIndex":
        find_first = command[1]
        z = text.find(find_first)
        print(z)

    elif command[0] == "Cut":
        start_from = command[1]
        start_from = int(start_from)
        length = command[2]
        length = int(length)
        diapazon = start_from + length
        results = text[start_from:diapazon]
        print(results)

    line = input()
