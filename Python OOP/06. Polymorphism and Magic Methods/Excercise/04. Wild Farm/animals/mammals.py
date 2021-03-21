from project.animals.animal import Mammal
from project.food import *

class Mouse(Mammal):
    def make_sound(self):
        return "Squeak"

    def feed(self, food: Food):
        if not isinstance(food, Vegetable) and not isinstance(food, Fruit):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 0.1
        self.food_eaten += food.quantity

class Dog(Mammal):
    def make_sound(self):
        return "Woof!"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 0.4
        self.food_eaten += food.quantity

class Cat(Mammal):
    def make_sound(self):
        return "Meow"

    def feed(self, food: Food):
        if not isinstance(food, Meat) and not isinstance(food, Vegetable):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 0.3
        self.food_eaten += food.quantity

class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 1.0
        self.food_eaten += food.quantity
