class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, new_rating):
        self.__rating = new_rating

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, new_players):
        self.__players = new_players