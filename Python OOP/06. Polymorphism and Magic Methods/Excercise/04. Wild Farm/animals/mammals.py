from project.animals.animal import Mammal
from project.food import *

class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food: Food):
        if type(food).__name__ != "Fruit" or type(food).__name__ != "Vegetable":
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        self.weight += food.quantity * 0.1
        self.food_eaten += food.quantity

class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food: Food):
        if type(food).__name__ != "Meat":
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        self.weight += food.quantity * 0.4
        self.food_eaten += food.quantity

class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food: Food):
        if type(food).__name__ != "Meat" or type(food).__name__ != "Vegetable":
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        self.weight += food.quantity * 0.3
        self.food_eaten += food.quantity

class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food: Food):
        if type(food).__name__ != "Meat":
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        self.weight += food.quantity * 1
        self.food_eaten += food.quantity
