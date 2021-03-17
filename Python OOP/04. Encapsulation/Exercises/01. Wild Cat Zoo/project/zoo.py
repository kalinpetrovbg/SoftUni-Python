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
            self.__animal_capacity -= 1
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        elif self.__animal_capacity > 0:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > 0:
            self.workers.append(worker)
            self.__workers_capacity -= 1
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        else:
            return f"Not enough space for worker"

    def fire_worker(self, worker_name):
        fired = [w for w in self.workers if w.name == worker_name][0]
        self.workers.remove(fired)
        self.__workers_capacity += 1
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        worker_cost = sum([w.salary for w in self.workers])
        if worker_cost < self.__budget:
            self.__budget -= worker_cost
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        tend_cost = sum([a.get_needs() for a in self.animals])
        if tend_cost < self.__budget:
            self.__budget -= tend_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount
        return self.__budget

    def animals_status(self):
        lions = [a for a in self.animals if type(a).__name__ == "Lion"]
        tigers = [a for a in self.animals if type(a).__name__ == "Tiger"]
        cheetahs = [a for a in self.animals if type(a).__name__ == "Cheetah"]
        lio = "\n".join(map(str, lions))
        tig = "\n".join(map(str, tigers))
        che = "\n".join(map(str, cheetahs))

        result = f"You have {len(self.animals)} animals\n"
        result += f"----- {len(lions)} Lions:\n"
        result += f"{lio}\n"
        result += f"----- {len(tigers)} Tigers:\n"
        result += f"{tig}\n"
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        result += f"{che}"
        return result

    def workers_status(self):
        keepers = [w for w in self.workers if type(w).__name__ == "Keeper"]
        caretakers = [w for w in self.workers if type(w).__name__ == "Caretaker"]
        vets = [w for w in self.workers if type(w).__name__ == "Vet"]
        kee = "\n".join(map(str, keepers))
        car = "\n".join(map(str, caretakers))
        vet = "\n".join(map(str, vets))

        result = f"You have {len(self.workers)} workers\n"
        result += f"----- {len(keepers)} Keepers:\n"
        result += f"{kee}\n"
        result += f"----- {len(caretakers)} Caretakers:\n"
        result += f"{car}\n"
        result += f"----- {len(vets)} Vet:\n"
        result += f"{vet}"
        return result