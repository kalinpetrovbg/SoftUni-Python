# numbers = [x for x in input().replace(" ", "").split("|")]
# result = [num for num in numbers[::-1]]
# print(' '.join("".join(str(x) for x in result)))

data = input().split("|")
data.reverse()
result = [value.strip() for i in range(len(data)) for value in data[i].split()]
print(*result)
