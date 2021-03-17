class Player:
    def __init__(self, name, endurance, sprint, dribble, passing, shooting):
        self.__name = name
        self.__endurance = endurance
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def endurance(self):
        return self.__endurance

    @endurance.setter
    def endurance(self, new_endurance):
        self.__endurance = new_endurance

    @property
    def sprint(self):
        return self.__sprint

    @sprint.setter
    def sprint(self, new_sprint):
        self.__sprint = new_sprint

    @property
    def dribble(self):
        return self.__dribble

    @dribble.setter
    def dribble(self, new_dribble):
        self.__dribble = new_dribble

    @property
    def passing(self):
        return self.__passing

    @passing.setter
    def passing(self, new_passing):
        self.__passing = new_passing

    @property
    def shooting(self):
        return self.__shooting

    @shooting.setter
    def shooting(self, new_shooting):
        self.__shooting = new_shooting

    def __str__(self):
        return f"""Player: {self.name}
Endurance: {self.endurance}
Sprint: {self.sprint}
Dribble: {self.dribble}
Passing: {self.passing}
Shooting: {self.shooting}
"""
