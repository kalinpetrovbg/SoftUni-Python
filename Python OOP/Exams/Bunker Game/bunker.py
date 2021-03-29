from project.survivor import Survivor
from project.supply.supply import Supply
from project.medicine.medicine import Medicine
from project.supply.supply import Supply
from project.supply.food_supply import FoodSupply
from project.supply.water_supply import WaterSupply

class Bunker:
    def __init__(self, survivors, supplies, medicine):
        self.survivors = list(survivors)
        self.supplies = list(supplies)
        self.medicine = list(medicine)
        self.__food = []
        self.__water = []
        self.__painkillers = []
        self.__salves = []

    @property
    def food(self):
        return self.__food

    def water(self):
        return self.__water

    def painkillers(self):
        return self.__painkillers

    def salves(self):
        return self.__salves

    def add_survivor(self, survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        else:
            self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type):
        if survivor.needs_healing:
            to_remove = [m for m in self.medicine if m.__class__.__name__ == medicine_type]
            Medicine.apply(self, survivor)
            self.medicine.remove(to_remove)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type):
        if survivor.needs_sustenance:
            to_remove = [f for f in self.food if f.__class__.__name__ == sustenance_type]
            Supply.apply(self, survivor)
            self.supplies.remove(to_remove)
            return f"{survivor.name} healed successfully with {sustenance_type}"

    def next_day(self):
        for s in self.survivors:
            s.needs -= (s.age * 2)

        for s in self.survivors
            Water.