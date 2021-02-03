males = [int(x) for x in input().split(" ") if int(x) != 0]
females = [int(x) for x in input().split(" ") if int(x) != 0]
matches = 0
fem = 0
man = 0

while True:

    for index in range(len(females)):
        if females[index] % 25 == 0 and females[index] != 0:
            females[index] = 0
            if 0 < index < len(females):
                females[index + 1] = 0

    for index in range(len(males)):
        if males[index] % 25 == 0 and males[index] != 0:
            males[index] = 0
            if 0 < index < len(males):
                males[index + 1] = 0

    females = list(filter(lambda x: x != 0, females))
    males = list(filter(lambda x: x != 0, males))

    if females[0] == males[-1]:
        females.pop(0)
        males.pop()
        matches += 1
    else:
        females.pop(0)
        males[-1] -= 2
        if males[-1] <= 0:
            males.pop()

    if not males:
        break
    if not females:
        break

if len(females) == 0:
    females.append("none")
if len(males) == 0:
    males.append("none")

print(f"Matches: {matches}")
print(f"Males left: {', '.join(map(str, males[::-1]))}")
print(f"Females left: {', '.join(map(str, females))}")
