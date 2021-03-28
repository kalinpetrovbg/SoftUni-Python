from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.laptop import Laptop
from project.appliances.fridge import Fridge
from project.people.child import Child

class YoungCoupleWithChildren(Room):
    def __init__(self, family_name, salary_one, salary_two, *children: Child):
        super().__init__(family_name, budget=salary_one+salary_two, members_count=2+len(children))
        self.room_cost = 30
        self.children = list(children)
        self.appliances = [TV(), Fridge(), Laptop()] * self.members_count
        self.__expenses = self.calculate_expenses()
        self.ch_expenses = sum([c.cost for c in self.children]) * 30
