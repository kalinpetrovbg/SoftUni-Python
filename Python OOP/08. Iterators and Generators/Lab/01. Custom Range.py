class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.index = start

    def __iter__(self):
        return self

    def __next__(self):
        while self.index > self.end:
            raise StopIteration
        value = self.index
        self.index += 1
        return value

one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
