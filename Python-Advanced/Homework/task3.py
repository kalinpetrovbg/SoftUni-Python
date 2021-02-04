import os

command = input()

while command != "End":
    action = command.split("-")

    if action[0] == "Create":
        file = open(action[1], "w")
        file.close()

    elif action[0] == "Add":
        file = open(action[1], "a")
        file.write(action[2] + "\n")
        file.close()

    elif action[0] == "Replace":
        try:
            file = open(action[1], 'r')
            file_data = file.read()
            new_data = file_data.replace(action[2], action[3])
            file = open(action[1], 'w')
            file.write(new_data)
            file.close()
        except:
            print("An error occurred")

    elif action[0] == "Delete":
        try:
            os.remove(action[1])
        except:
            print("An error occurred")

    command = input()