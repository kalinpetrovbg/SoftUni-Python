def even_odd(*args):
    command = args[-1]
    if command == "even":
        return list(filter(lambda x: x % 2 == 0, args[:-1]))
    else:
        return list(filter(lambda x: x % 2 != 0, args[:-1]))

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
