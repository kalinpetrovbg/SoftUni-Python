from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament


class Controller:
    def __init__(self):
        self.decorations_repository: DecorationRepository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type, aquarium_name):
        if aquarium_type != "FreshwaterAquarium" and aquarium_type != "SaltwaterAquarium":
            return "Invalid aquarium type."                     # potential problem
        if aquarium_type == "FreshwaterAquarium":
            self.aquariums.append(FreshwaterAquarium(aquarium_name))
            return "Successfully added FreshwaterAquarium."
        if aquarium_type == "SaltwaterAquarium":
            self.aquariums.append(SaltwaterAquarium(aquarium_name))
            return "Successfully added SaltwaterAquarium."

    def add_decoration(self, decoration_type):
        if decoration_type != "Ornament" and decoration_type != "Plant":
            return "Invalid decoration type."
        if decoration_type == "Ornament":
            self.decorations_repository.add(decoration_type)
            return "Successfully added Ornament."
        if decoration_type == "Plant":
            self.decorations_repository.add(decoration_type)
            return "Successfully added Plant."

    def insert_decoration(self, aquarium_name, decoration_type):
        try:
            de = [d for d in self.decorations_repository.decorations if d == decoration_type][0]
        except IndexError:
            return f"There isn't a decoration of type {decoration_type}."

        try:
            aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
            decoration = [d for d in self.decorations_repository.decorations if d == decoration_type][0]
            aquarium.add_decoration(decoration)
            self.decorations_repository.decorations.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."
        except IndexError:
            return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        if fish_type != "FreshwaterFish" and fish_type != "SaltwaterFish":
            return f"There isn't a fish of type {fish_type}."

        aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]

        aquarium.add_fish(fish_name, fish_species, price)          # maybe with return

    def feed_fish(self, aquarium_name):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
        aquarium.feed()                                         # maybe with return
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]

        fish_value = sum([f.price for f in aquarium.fish])
        decorations_value = sum([d.price for d in aquarium.decorations])
        value = fish_value + decorations_value

        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        result = ""
        for a in self.aquariums:
            result += f"{a}\n"
        return result
