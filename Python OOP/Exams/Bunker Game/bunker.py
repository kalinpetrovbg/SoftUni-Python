class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        list_of_foods = [x for x in self.supplies if x.__class__.__name__ == 'FoodSupply']
        if len(list_of_foods) == 0:
            raise IndexError('There are no food supplies left!')
        return list_of_foods

    @property
    def water(self):
        list_of_waters = [x for x in self.supplies if x.__class__.__name__ == 'WaterSupply']
        if len(list_of_waters) == 0:
            raise IndexError('There are no water supplies left!')
        return list_of_waters

    @property
    def painkillers(self):
        list_of_painkillers = [x for x in self.medicine if x.__class__.__name__ == 'Painkiller']
        if len(list_of_painkillers) == 0:
            raise IndexError('There are no painkillers left!')
        return list_of_painkillers

    @property
    def salves(self):
        list_of_salves = [x for x in self.medicine if x.__class__.__name__ == 'Salve']
        if len(list_of_salves) == 0:
            raise IndexError('There are no salves left!')
        return list_of_salves

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f'Survivor with name {survivor.name} already exists.')
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        if survivor.needs_healing:
            if medicine_type == "Salve":
                current = self.salves.pop()
            else:
                current = self.painkillers.pop()
            self.medicine.remove(current)
            current.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"
        return

    def sustain(self, survivor, sustenance_type):
        if survivor.needs_sustenance:
            if sustenance_type == "FoodSupply":
                current = self.food.pop()
            else:
                current = self.water.pop()
            self.supplies.remove(current)
            current.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"
        return

    def next_day(self):
        for each in self.survivors:
            each.needs -= (each.age * 2)
            self.sustain(each, "FoodSupply")
            self.sustain(each, "WaterSupply")
