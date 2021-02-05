people = int(input())
capacity = [int(el) for el in input().split(" ")]
max_people = people

while people > 0:

    if sum(capacity) == len(capacity) * 4:
        break

    for wagon in range(len(capacity)):
        while not capacity[wagon] == 4:
            capacity[wagon] += 1
            people -= 1

            if people == 0:
                break

        if people == 0:
            break

if people == 0:
    if len(capacity) * 4 > sum(capacity):
        print("The lift has empty spots!")

elif people > 0:
    print(f"There isn't enough space! {people} people in a queue!")

print(*capacity, sep=" ")