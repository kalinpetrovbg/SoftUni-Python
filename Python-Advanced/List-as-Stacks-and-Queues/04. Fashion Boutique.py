clothes = input().split()
MAX_CAPACITY = int(input())
stack = [int(x) for x in clothes]
current = 0
racks = 1

while len(stack) > 0:
    item = stack.pop()
    current += item
    if current <= MAX_CAPACITY:
        continue
    else:
        racks += 1
        current = item

print(racks)
