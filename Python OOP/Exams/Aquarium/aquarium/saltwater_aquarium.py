from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    def __init__(self, name):
        super().__init__(name, capacity=25)
        self.decorations = []
        self.fish = []