original = [1, 2, 3, 2, 1, 4, 2, 1]

unique = sorted(set(original), key=original.index)

print(unique)
