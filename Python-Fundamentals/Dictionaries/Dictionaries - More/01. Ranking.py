text = input()
contests = {}
students = {}
best_person = ""
best_score = 0

while text != "end of contests":
    contest, password = text.split(":")
    contests[contest] = password
    text = input()

data = input()

while data != "end of submissions":

    exam, passw, user, points = data.split("=>")
    if exam in contests and passw == contests[exam]:
        points = int(points)
        if user not in students:
            students[user] = {exam: points}
        else:
            if exam in students[user]:
                if students[user][exam] < points:
                    students[user][exam] = points
            else:
                students[user][exam] = points
    data = input()

final = {}

for name, stats in students.items():
    for exams, points in stats.items():
        points = int(points)
        if name not in final:
            final[name] = points
        else:
            final[name] += points

for person, score in final.items():
    if score > best_score:
        best_score = score
        best_person = person

print(f"Best candidate is {best_person} with total {best_score} points.")
print("Ranking:")

for name, stats in sorted(students.items(), key=lambda x: x[0]):
    print(name)
    for exams, points in sorted(stats.items(), key=lambda x: -x[1]):
        print(f"#  {exams} -> {points}")