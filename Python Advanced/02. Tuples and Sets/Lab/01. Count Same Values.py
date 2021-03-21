values = input().split()

result = {}

for each in values:
    each = float(each)
    if each not in result:
        result[each] = 1
    else:
        result[each] += 1

for (num, times) in result.items():
    print(f"{num} - {times} times")