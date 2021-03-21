class Animal:
        def __init__(self, species):
            self.species = species

        def get_species(self):
            return self.species


class Cat(Animal):
    def make_sound(self):
        return 'meow'

class Dog(Animal):
    def make_sound(self):
        return 'woof-woof'


def animal_sound(animals):
    for a in animals:
        a.make_sound()


animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
animal_sound(animals)
