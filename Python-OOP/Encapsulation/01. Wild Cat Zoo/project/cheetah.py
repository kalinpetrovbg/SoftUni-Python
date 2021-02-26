class Cheetah:
    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age
        self.type = 'Cheetah'

    @staticmethod
    def get_needs(self):
        return 60

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"