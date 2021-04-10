from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    fish_type = "FreshwaterFish"

    def __init__(self, name, species, price):
        super().__init__(name, species, size=3, price=price)
        self.eat_value = 3

