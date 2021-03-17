from project.animal import Animal

class Dog(Animal):
    def __init__(self):
        pass

    @staticmethod
    def bark():
        return f"barking..."
