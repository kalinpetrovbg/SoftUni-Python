from project.animals.animal import Mammal


class Mouse(Mammal):
    @staticmethod
    def make_sound():
        return "Squeak"

class Dog(Mammal):
    @staticmethod
    def make_sound():
        return "Woof!"

class Cat(Mammal):
    @staticmethod
    def make_sound():
        return "Meow"

class Tiger(Mammal):
    @staticmethod
    def make_sound():
        return "ROAR!!!"