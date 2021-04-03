class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = sum([r.expenses + r.room_cost for r in self.rooms])
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        res = []
        for room in self.rooms:
            if room.budget >= room.expenses + room.room_cost:
                res.append(f"{room.family_name} paid {room.expenses + room.room_cost:.2f}$ and "
                           f"have {room.budget:.2f}$ left.")
                room.budget -= room.expenses + room.room_cost
            else:
                res.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)
        return "\n".join(res)

    def status(self):
        total_members = sum([r.members_count for r in self.rooms])
        print(f"Total population: {total_members}")
        res = []
        for r in self.rooms:
            res.append(f"{r.family_name} with {r.members_count} members. "
                       f"Budget: {r.budget:.2f}$, Expenses: {r.expenses:.2f}$")
            num = 0
            for c in r.children:
                num += 1
                res.append(f"--- Child {num} monthly cost: {c.cost * 30:.2f}$")
            res.append(f"--- Appliances monthly cost: {r.expenses - r.child_expenses:.2f}$")
        return "\n".join(res)