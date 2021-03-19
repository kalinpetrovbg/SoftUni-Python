from project.product import Product

class Beverage(Product):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price)
        self.milliliters = milliliters
