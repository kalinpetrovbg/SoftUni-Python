def fibonacci():
    first = 0
    second = 1
    while True:
        yield first
        new = first + second
        first = second
        second = new

generator = fibonacci()
for i in range(5):
    print(next(generator))
