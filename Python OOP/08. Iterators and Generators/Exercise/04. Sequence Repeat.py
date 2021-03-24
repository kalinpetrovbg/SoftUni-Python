class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.number:
            raise StopIteration
        while len(self.sequence) < self.number:
            self.sequence += self.sequence
        letter = self.sequence[self.index]
        self.index += 1
        return letter


result = sequence_repeat('abc', 20)
for item in result:
    print(item, end ='')
