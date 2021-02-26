from cheetah import Cheetah
from lion import Lion
from tiger import Tiger
from keeper import Keeper
from caretaker import Caretaker
from vet import Vet

class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.__budget = budget
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price <= self.__budget and self.__animal_capacity > 0:
            self.animals.append(animal)
            self.__budget -= price
            return f"{self.animal} the {animal} added to the zoo"
        if self.__animal_capacity > 0 and price > self.__budget:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > 0:
            self.workers.append(worker)
        else:
            return f"Not enough space for worker"

    def fire_worker(self, worker_name):
        if worker_name in self.workers:
            self.workers.remove(worker_name)
            return f"{worker_name} fired successfully"

    def pay_workers(self):
        if self.__budget >= len(self.workers):  #  to do
            return f"You payed your workers. They are happy. Budget left: {self.budget}"
        else:
            return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        if self.__budget > 0:
            pass

    def profit(self, amount):
        self.__budget += amount

    def animals_satus(self):
        pass

    def workers_status(self):
        pass

zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
