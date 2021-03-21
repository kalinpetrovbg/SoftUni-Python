from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, weight, food_eaten=0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass

class Bird(ABC):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

class Mammal(ABC):
    def __init__(self, living_region):
        self.living_region = living_region
