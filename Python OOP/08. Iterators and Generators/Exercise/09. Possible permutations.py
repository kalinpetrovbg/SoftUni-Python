from itertools import permutations

def possible_permutations(ll):
    perm = permutations(ll)
    for i in list(perm):
        yield list(i)


[print(n) for n in possible_permutations([1, 2, 3])]