from project.appliances.appliance import Appliance

class Stove(Appliance):
    def __init__(self, cost=0.7):
        super().__init__(cost)