from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.laptop import Laptop
from project.appliances.fridge import Fridge

class YoungCouple(Room):
    def __init__(self, family_name, salary_one, salary_two):
        super().__init__(family_name, budget=salary_one+salary_two, members_count=2)
        self.room_cost = 20
        self.children = []
        self.appliances = [TV(), Fridge(), Laptop()] * 2
        self.__expenses = self.calculate_expenses()
