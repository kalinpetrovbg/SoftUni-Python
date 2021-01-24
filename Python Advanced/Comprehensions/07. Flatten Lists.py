numbers = [x for x in input().replace(" ", "").split("|")]
result = [num for num in numbers[::-1]]
print(' '.join("".join(str(x) for x in result)))
