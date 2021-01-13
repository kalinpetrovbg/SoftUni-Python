num = int(input())

students = {}

for _ in range(num):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = []
    students[name].append(grade)

filtered_students = {}

for name, grade in students.items():
    result = sum(grade) / len(grade)
    if result >= 4.50:
        filtered_students[name] = result

for name, result in sorted(filtered_students.items(), key=lambda x: x[1], reverse=True):
    print(f"{name} -> {result:.2f}")
