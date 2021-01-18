number = int(input())
grades = {}

for _ in range(number):
    name, grade = input().split()
    grade = float(grade)

    if name not in grades:
        grades[name] = []
        grades[name].append(grade)
    else:
        grades[name].append(grade)

for (name, grade) in grades.items():
    grades_string = " ".join(map(str,grade))
    average = sum(grade) / len(grade)
    print(f"{name} -> {grades_string:.2f} (avg: {average:.2f})")