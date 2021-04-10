from abc import ABC, abstractmethod


class BaseFish(ABC):
    fish_type = ""

    def __init__(self, name, species, size, price: float):
        self.name = name
        self.species = species
        self.size = size
        self.price = price
        self.eat_value = 5

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Fish name cannot be an empty string.")
        self._name = value

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, value):
        if value == "":
            raise ValueError("Fish species cannot be an empty string.")
        self._species = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price cannot be equal to or below zero.")
        self._price = value

    def eat(self):
        self.size += self.eat_value


