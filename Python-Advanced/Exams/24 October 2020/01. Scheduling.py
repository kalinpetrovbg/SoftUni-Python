tasks = [int(x) for x in input().split(", ")]
target = int(input())
result = 0

while True:
    for _ in range(len(tasks)):
        m = min(tasks)
        result += m
        current = tasks.index(m)
        if current is target:
            break
        else:
            tasks[current] = 9999
    break

print(result)
