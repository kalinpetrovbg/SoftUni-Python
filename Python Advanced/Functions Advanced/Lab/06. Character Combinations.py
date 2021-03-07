from itertools import permutations

names = list(input())
print(*[f"{''.join(x)}" for x in list(permutations(names))], sep="\n")