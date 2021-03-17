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

    def add_player(self, player):
        if player not in self.players:
            self.players.append(player)
            return f"Player {player.name} joined team {self.name}"
        return f"Player {player.name} has already joined"

    def remove_player(self, player_name):
        try:
            to_remove = [p for p in self.players if p.name == player_name][0]
            self.players.remove(to_remove)
            return to_remove
        except IndexError:
            return f"Player {player_name} not found"
