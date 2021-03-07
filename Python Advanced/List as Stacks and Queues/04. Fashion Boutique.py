clothes = [int(x) for x in input().split()]
capacity = int(input())
racks = 1
current = capacity

while clothes:
    if clothes[-1] > current:
        current = capacity
        racks += 1
    current -= clothes[-1]
    clothes.pop()

print(racks)
