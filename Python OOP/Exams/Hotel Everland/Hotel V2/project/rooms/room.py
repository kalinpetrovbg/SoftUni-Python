class Room:
    def __init__(self, family_name, budget, members_count):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.appliances = []
        self._expenses = self.calculate_expenses()
        self.child_expenses = 0

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        else:
            self._expenses = value

    def calculate_expenses(self, *args):
        ll = self.appliances + self.children
        value = round(sum([element.cost for element in ll]), 2)
        self.expenses = value
        return value
