person_1 = int(input())
person_2 = int(input())
person_3 = int(input())
capacity = person_1 + person_2 + person_3
students = int(input())

hour = 0

while students > 0:
    students -= capacity
    hour += 1

    if hour % 4 == 0:
        hour += 1

print(f"Time needed: {hour}h.")
