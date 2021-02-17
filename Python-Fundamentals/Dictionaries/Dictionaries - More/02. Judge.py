data = input()
results = {}
totals = {}

while data != "no more time":

    username, contest, points = data.split(" -> ")
    points = int(points)

    if username not in totals:
        totals[username] = points
    else:
        totals[username] += points

    if contest not in results:
        if username not in results:
            results[contest] = {username: points}
        else:
            if results[contest][username] < points:
                results[contest][username] = points
    else:
        results[contest][username] = points

    data = input()





print("Individual standings:")
nums = 0
for name, score in sorted(totals.items(), key=lambda x: -x[1]):
    nums += 1
    print(f"{nums}. {name} -> {score}")
