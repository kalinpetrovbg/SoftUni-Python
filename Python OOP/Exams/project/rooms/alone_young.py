from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.laptop import Laptop
from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.people.child import Child

class AloneYoung(Room):
    def __init__(self, family_name, salary):
        super().__init__(family_name, budget=salary, members_count=1)
        self.room_cost = 10
        self.children = []
        self.appliances = [TV()]
        self.__expenses = self.calculate_expenses()
