class Tiger:
    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age
        self.type = 'Tiger'

    @staticmethod
    def get_needs(self):
        return 45

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"