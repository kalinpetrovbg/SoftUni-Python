from project.beverage.hot_beverage import HotBeverage

class Coffee(HotBeverage):
    def __init__(self, name, price, milliliters, caffeine):
        super().__init__(name, price, milliliters)
        self.MILLILITERS = 50
        self.PRICE = 3.50
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine
