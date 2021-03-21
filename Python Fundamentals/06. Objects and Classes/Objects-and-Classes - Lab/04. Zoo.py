class Zoo:
    animals = 0

    def __init__(self, name_zoo):
        self.name_zoo = name_zoo
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f"Mammals in {self.name_zoo}: {', '.join(self.mammals)}"
        elif species == "fish":
            return f"Fishes in {self.name_zoo}: {', '.join(self.fishes)}"
        elif species == "bird":
            return f"Birds in {self.name_zoo}: {', '.join(self.birds)}"


zoo_name = input()
zoo = Zoo(zoo_name)

count = int(input())

for _ in range(count):
    animal = input()
    species, name = animal.split(" ")
    zoo.add_animal(species, name)

info = input()
print(zoo.get_info(info))
print(f"Total animals: {Zoo.animals}")