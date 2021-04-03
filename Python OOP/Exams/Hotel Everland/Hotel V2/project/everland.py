class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)    # what if same room is appended twice?

    def get_monthly_consumptions(self):
        total_consumption = sum([r.expenses+r.room_cost for r in self.rooms])
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        for r in self.rooms:
            if r.budget > r.expenses+r.room_cost:
                old_budget = r.budget
                new_budget = r.budget - r.expenses+r.room_cost
                r.budget = new_budget
                return f"{r.family_name} paid {r.expenses+r.room_cost}$ and have {old_budget:.2f}$ left."
            else:
                self.rooms.remove(r)
                return f"{r.family_name} does not have enough budget and must leave the hotel."

    def status(self):
        total_members = sum([r.members_count for r in self.rooms])
        print(f"Total population: {total_members}")