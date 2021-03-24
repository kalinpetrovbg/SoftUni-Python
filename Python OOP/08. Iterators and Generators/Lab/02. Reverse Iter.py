class reverse_iter:
    def __init__(self, ll):
        self.list = list(ll)
        self.index = len(self.list) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        number = self.list[self.index]
        self.index -= 1
        return number

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
