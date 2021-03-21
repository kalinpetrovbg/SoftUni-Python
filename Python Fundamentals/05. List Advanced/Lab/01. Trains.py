wagons = int(input())
train = [0] * wagons

command = input()

while not command == "End":
    data = command.split()

    if "add" in data:
        number_people = int(data[1])
        train[-1] += number_people

    if "insert" in data:
        index = int(data[1])
        number_people = int(data[2])
        train[index] += number_people

    if "leave" in data:
        index = int(data[1])
        number_people = int(data[2])
        train[index] -= number_people

    if "End" in data:
        break

    command = input()

print(train)

