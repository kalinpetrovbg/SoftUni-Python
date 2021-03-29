class Survivor:
    def __init__(self, name, age, health=100, needs=100):

        if name == "":
            raise ValueError("Name not valid!")
        else:
            self.name = name
        if age < 0:
            raise ValueError("Age not valid!")
        else:
            self.age = age

        if health < 0:
            raise ValueError("Health not valid!")
        else:
            self.health = 100
        if needs < 0:
            raise ValueError("Needs not valid!")
        self.needs = 100
        if self.needs < 100:
            self.__needs_sustenance = True
        else:
            self.__needs_sustenance = False
        if self.health < 100:
            self.__needs_healing = True
        else:
            self.__needs_healing = False

    @property
    def needs_sustenance(self):
        return self.__needs_sustenance

    @property
    def needs_healing(self):
        return self.__needs_healing

#
# s = Survivor("Kalin", 34)
#
# print(s.health)
# print(s.needs)
# print(s.name)
# s.needs = -55
# print(s.needs)