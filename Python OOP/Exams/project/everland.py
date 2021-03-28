from project.rooms.room import Room

class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        expenses = sum([room.expenses for room in self.rooms])
        room_costs = sum([room.room_cost for room in self.rooms])
        total = expenses + room_costs
        return f"Monthly consumption: {total:.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            if room.budget >= room.expenses + room.room_cost:
                result.append(f"{room.family_name} paid {room.expenses + room.room_cost:.2f}$ and "
                              f"have {room.budget:.2f}$ left.")
                room.budget -= room.expenses + room.room_cost
            else:
                result += f"{room.family_name} does not have enough budget and must leave the hotel."
                self.rooms.remove(room)
        return "\n".join(result)

    def status(self):
        result = []
        result.append(f"Total population: {sum([room.members_count for room in self.rooms])}")
        for room in self.rooms:
            result.append(f"{room.family_name} with {room.members_count} members. "
                          f"Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$")
            num = 0
            for child in room.children:
                num += 1
                result.append(f"--- {child.__class__.__name__} {num} monthly cost: {30 * child.cost:.2f}$")
            result.append(f"--- Appliances monthly cost: {room.expenses - room.ch_expenses:.2f}$")
        return "\n".join(result)