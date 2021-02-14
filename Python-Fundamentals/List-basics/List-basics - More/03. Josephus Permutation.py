def josephus(soldier, skip):
    skip -= 1                       # pop automatically skips the dead guy
    index = skip % len(soldier)
    while len(soldier) > 1:
        dead = soldier.pop(index)   # kill soldier at idx
        index = (index + skip) % len(soldier)
        new.append(dead)
    new.extend(soldier)
    return new

nums = [x for x in input().split(" ")]
n = int(input())
new = []

res = josephus(nums, n)
print(f'[{",".join(str(x) for x in res)}]')