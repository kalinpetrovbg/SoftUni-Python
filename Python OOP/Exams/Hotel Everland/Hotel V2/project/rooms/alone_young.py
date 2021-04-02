from project.rooms.room import Room
from project.appliances.tv import TV


class AloneOld(Room):
    def __init__(self, family_name, pension):
        super().__init__(family_name, budget=pension, members_count=1)
        self.room_cost = 10
        self.appliances = [TV()]
        self.expenses = self.calculate_expenses(self.appliances)


a = AloneOld("petrov", 100)
print(a.expenses)