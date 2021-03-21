from project.animals.animal import Bird
from project.food import *

class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if type(food).__name__ != "Meat":
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        self.weight += food.quantity * 0.25
        self.food_eaten += food.quantity

class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food: Food):
        self.weight += food.quantity * 0.35
        self.food_eaten += food.quantity



owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)
