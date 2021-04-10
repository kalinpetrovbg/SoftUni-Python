from project.decoration.base_decoration import BaseDecoration


class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        try:
            de = [d for d in self.decorations if d.__class__.__name__ == decoration.__class__.__name__][0]
            self.decorations.remove(de)
            return True
        except IndexError:
            return False

    def find_by_type(self, decoration_type):
        try:
            found = [d for d in self.decorations if d.__class__.__name__ == decoration_type][0]
            return found
        except IndexError:
            return "None"
