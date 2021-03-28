class Room:
    def __init__(self, family_name, budget, members_count):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.appliances = []
        self.__expenses = self.calculate_expenses()
        self.ch_expenses = sum([c.cost for c in self.children])

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, new_expenses):
        if new_expenses < 0:
            raise ValueError("Expenses cannot be negative")
        else:
            self.__expenses = new_expenses

    def calculate_expenses(self, *args):
        args = self.appliances + self.children
        self.__expenses = round(sum([x.cost for x in args]) * 30, 2)
        new_expenses = self.expenses
        return new_expenses
