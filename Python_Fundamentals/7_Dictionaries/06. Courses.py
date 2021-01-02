command = input()
output = {}
counter = {}

while command != "end":
    course, name = command.split(" : ")
    if course not in output:
        output[course] = []
        output[course].append(name)
        counter[course] = 1
    else:
        output[course].append(name)
        counter[course] += 1

    command = input()

for course, name in sorted(counter.items(), key=lambda x: x[1], reverse=True):
    print(f"{course}: {name}")

    for courses, names in sorted(output.items(), key=lambda x: x[1]):
        if courses == course:
            names = sorted(names)
            z = [f"-- {person}" for person in names]
            print('\n'.join(z))