class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.count:
            raise StopIteration
        for num in range(self.index, self.count):
            result = num * self.step
            self.index += 1
            return result


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
