from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.laptop import Laptop
from project.appliances.fridge import Fridge


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name, salary_one, salary_two, *children):
        super().__init__(family_name, budget=salary_one+salary_two, members_count=2 + len(children))
        self.children = list(children)
        self.room_cost = 30
        self.appliances = [TV(), Fridge(), Laptop()] * self.members_count
        self._expenses = self.calculate_expenses() * 30
        self.child_expenses = sum([c.cost for c in self.children]) * 30
