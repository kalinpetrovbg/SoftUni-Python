def squares(num):
    for x in range(1, num + 1):
        yield x ** 2

print(list(squares(5)))