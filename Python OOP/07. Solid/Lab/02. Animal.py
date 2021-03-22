from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species

    @abstractmethod
    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        return 'meow'

class Dog(Animal):
    def make_sound(self):
        return 'woof-woof'

class Chicken(Animal):
    def make_sound(self):
        return "chick-chirik"

def animal_sound(animals: list[Animal]):
    for animal in animals:
        print(animal.make_sound())


animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
animal_sound(animals)
