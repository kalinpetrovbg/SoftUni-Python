data = input()
results = {}
totals = {}

while data != "no more time":

    username, contest, points = data.split(" -> ")
    points = int(points)

    if contest not in results:

        if username not in totals:
            totals[username] = points
        else:
            totals[username] += points

        if username not in results:
            results[contest] = {username: points}
        else:
            if results[contest][username] < points:
                results[contest][username] = points
    else:
        results[contest][username] = points
        if username not in totals:
            totals[username] = points
        else:
            if totals[username] < points:
                totals[username] += points

    data = input()

for course, stats in results.items():
    print(f"{course}: {len(stats)} participants")
    count = 0
    for name, res in sorted(stats.items(), key=lambda x: -x[1]):
        count += 1
        print(f"{count}. {name} <::> {res}")

print("Individual standings:")
nums = 0
for name, score in sorted(totals.items(), key=lambda x: -x[1]):
    nums += 1
    print(f"{nums}. {name} -> {score}")
