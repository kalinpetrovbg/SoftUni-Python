xy = [int(el) for el in input().split(", ")]

even = [index for index in range(len(xy)) if xy[index] % 2 == 0]
# evens = list(filter(lambda x: x % 2 == 0, xy))

print(even)