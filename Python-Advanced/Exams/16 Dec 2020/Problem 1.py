males = [int(x) for x in input().split(" ") if int(x) > 0][::-1]
females = [int(x) for x in input().split(" ") if int(x) > 0]
matches = 0

for index in range(len(males)):
    if males[index] % 25 == 0:
        males[index] = -1
        if index + 1 < len(males):
            males[index + 1] = -1
males = [x for x in males if x != -1]

for index in range(len(females)):
    if females[index] % 25 == 0:
        females[index] = -1
        if index + 1 < len(females):
            females[index + 1] = -1
females = [x for x in females if x != -1]

while males and females:

    if females[0] == males[0]:
        females.pop(0)
        males.pop(0)
        matches += 1
    else:
        females.pop(0)
        males[0] -= 2
        if males[0] <= 0:
            males.pop(0)

print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join(map(str, males))}")
else:
    print(f"Males left: none")
if females:
    print(f"Females left: {', '.join(map(str, females))}")
else:
    print(f"Females left: none")
