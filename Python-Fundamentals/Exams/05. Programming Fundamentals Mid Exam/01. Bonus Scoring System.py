import math
students = int(input())
lectures = int(input())
start_bonus = int(input())
biggest_bonus = 0
num_attendance = 0

for student in range(students):

    attendance = int(input())
    total_bonus = attendance / lectures * (5 + start_bonus)

    if total_bonus > biggest_bonus:
        biggest_bonus = total_bonus
        num_attendance = attendance

print(f"Max Bonus: {math.ceil(biggest_bonus)}.")
print(f"The student has attended {num_attendance} lectures.")

