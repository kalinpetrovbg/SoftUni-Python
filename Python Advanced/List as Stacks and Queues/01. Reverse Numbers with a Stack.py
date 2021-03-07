new = [x for x in input().split()]
result = []

while len(new) > 0:
    result.append(new.pop())

print(" ".join(result))