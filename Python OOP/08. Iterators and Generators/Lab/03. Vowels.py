class vowels:
    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.string) - 1:
            raise StopIteration
        current_letter = self.string[self.index]
        self.index += 1
        if current_letter.lower() in "aeoiyu":
            return current_letter
        return self.__next__()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
