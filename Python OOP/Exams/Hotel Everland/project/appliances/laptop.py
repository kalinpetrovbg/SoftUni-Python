from project.appliances.appliance import Appliance

class Laptop(Appliance):
    def __init__(self, cost=1.0):
        super().__init__(cost)