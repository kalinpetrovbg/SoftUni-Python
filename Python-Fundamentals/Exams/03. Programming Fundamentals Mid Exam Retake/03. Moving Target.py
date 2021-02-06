numbers = [int(el) for el in input().split()]
text = input()

while not text == "End":
    command, index, power = text.split()
    index = int(index)
    power = int(power)

    if "Shoot" in text:
        if 0 <= index < len(numbers):
            numbers[index] -= power
            if numbers[index] <= 0:
                numbers.pop(index)

    elif "Add" in text:
        if 0 <= index < len(numbers):
            numbers.insert(index, power)
        else:
            print("Invalid placement!")

    elif "Strike" in text:
        minimum = index - power
        maximum = index + power

        if minimum >= 0 and maximum < len(numbers):
            del numbers[minimum: maximum + 1]
        else:
            print("Strike missed!")

    text = input()

print('|'.join(list(map(str, numbers))))
