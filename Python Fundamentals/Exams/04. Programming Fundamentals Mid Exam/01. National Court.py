staff1 = int(input())
staff2 = int(input())
staff3 = int(input())
efficiency = staff1 + staff2 + staff3
people = int(input())
time = 0

while people > 0:

    people -= efficiency
    time += 1

    if time % 4 == 0:
        time += 1

print(f"Time needed: {time}h.")



