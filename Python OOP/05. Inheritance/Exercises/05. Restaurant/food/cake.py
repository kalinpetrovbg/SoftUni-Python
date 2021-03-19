from project.food.dessert import Dessert

class Cake(Dessert):
    def __init__(self, name):
        super().__init__(name, price=self.PRICE, grams=self.GRAMS, calories=self.CALORIES)
        self.GRAMS = 250
        self.CALORIES = 1000
        self.PRICE = 5