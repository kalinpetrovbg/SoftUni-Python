from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self._name = value

    def calculate_comfort(self):
        comfort = sum([d.comfort for d in self.decorations])
        return comfort

    def add_fish(self, fish):
        fish_type = fish.__class__.__name__

        if len(self.fish) >= self.capacity:
            return "Not enough capacity."

        if self.__class__.__name__ == "FreshwaterAquarium" and fish_type != "FreshwaterFish":
            return "Water not suitable."
        if self.__class__.__name__ == "SaltwaterAquarium" and fish_type != "SaltwaterFish":
            return "Water not suitable."

        self.fish.append(fish)
        return f"Successfully added {fish_type} to {self.name}."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for f in self.fish:
            f.eat()

    def __str__(self):
        fifi = " ".join(f.name for f in self.fish)

        result = f"{self.name}:\n"
        if len(self.fish) == 0:
            result += f"Fish: none\n"
        else:
            result += f"Fish: {fifi}\n"
        result += f"Decorations: {len(self.decorations)}\n"
        result += f"Comfort: {self.calculate_comfort()}"
        return result
