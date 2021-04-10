from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.base_fish import BaseFish
from project.controller import Controller


# Aquariums
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish

b = BaseAquarium("Base", 10)
f = FreshwaterAquarium("FreshAQ")
s = SaltwaterAquarium("SaltAQ")

# Fish
fish1 = BaseFish("BaseF", "G", 10, 100)
fish2 = FreshwaterFish("FreshF", "FF", 200)
fish3 = SaltwaterFish("FreshF", "FF", 200)

# Decorations
decor1 = Ornament()
decor2 = Plant()

# Decor Repos
de = DecorationRepository()

# Controllers
co = Controller()

print(s.add_fish(fish2))
print(s.add_fish(fish2))
print(s.add_fish(fish3))
print(s.add_fish(fish3))
print(s.add_fish(fish3))
s.remove_fish(fish3)
print(len(s.fish))
s.add_decoration(decor1)
s.add_decoration(decor1)
s.add_decoration(decor2)
s.add_decoration(decor2)
print(len(s.decorations))
print(s.calculate_comfort())
print(sum([d.price for d in s.decorations]))
print(f"Size: {fish3.size}")
print(s.feed())
print(s.feed())
print(f"Size: {fish3.size}")
print(f"Fish numbersssss: {len(s.fish)}")
print(s)
print(fish3.fish_type)

print(co.add_aquarium("SaltwaterAquarium", "SaltAQ"))
print(co.add_aquarium("FreshwaterAquarium", "FreshAQ"))
print(len(co.aquariums))
print(co.add_decoration("Plant"))
print(co.add_decoration("Ornament"))
print(co.add_decoration("Kurec"))
print(de.decorations)
de.add(Plant())
de.add(Ornament())
de.add(Plant())
print(len(de.decorations))
print(de.remove(Plant()))
print(len(de.decorations))
print(de.find_by_type("Plant"))
print(de.find_by_type("Ornament"))
print(co.add_decoration("Plant"))
print(co.add_decoration("Ornament"))
print(co.add_decoration("Ornamentdas"))
print(len(co.decorations_repository.decorations))
print(len(s.decorations))
print(co.insert_decoration("SaltAQ", "Plantаааааа"))
print(co.decorations_repository.decorations)
print(len(s.decorations))
print(len(s.fish))
print(co.feed_fish("SaltAQ"))
print(co.calculate_value("SaltAQ"))
print(co.report())

print(s.add_fish(fish2))
print(s.add_fish(fish2))
print(s.add_fish(fish3))
print(s.add_fish(fish3))
print(s.add_fish(fish3))
s.remove_fish(fish3)
print(len(s.fish))
s.add_decoration(decor1)
s.add_decoration(decor1)
s.add_decoration(decor2)
s.add_decoration(decor2)


print(co.feed_fish("SaltAQ"))
print(co.calculate_value("SaltAQ"))
print(co.report())