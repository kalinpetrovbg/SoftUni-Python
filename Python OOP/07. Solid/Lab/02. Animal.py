class Animal:
    pass

class Cat(Animal):
    def animal_sound(self):
        return 'meow'

class Dog(Animal):
    def animal_sound(self):
        return 'woof-woof'


def animal_sound(animals):
    for a in animals:
        return a.animal_sound()


animals = [Cat(), Dog()]
print(animal_sound(animals))

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
