from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    fish_type = "SaltwaterFish"

    def __init__(self, name, species, price):
        super().__init__(name, species, size=5, price=price)
        self.eat_value = 2

