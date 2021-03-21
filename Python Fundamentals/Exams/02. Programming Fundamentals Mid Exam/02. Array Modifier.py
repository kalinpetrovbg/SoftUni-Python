numbers = [int(el) for el in input().split()]
text = input()

while not text == "end":

    if "swap" in text:
        command, index1, index2 = text.split()
        index1 = int(index1)
        index2 = int(index2)
        numbers[index1], numbers[index2] = numbers[index2], numbers[index1]

    elif "multiply" in text:
        command, index1, index2 = text.split()
        index1 = int(index1)
        index2 = int(index2)
        numbers[index1] *= numbers[index2]

    elif "decrease" in text:
        numbers = [num - 1 for num in numbers]

    text = input()

print(*numbers, sep=", ")
