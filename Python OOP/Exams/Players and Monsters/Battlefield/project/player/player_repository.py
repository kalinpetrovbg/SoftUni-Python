from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add_player(self, player: Player):
        try:
            pl = [p for p in self.players if p.username == player.username][0]
            raise ValueError(f"Player {pl.username} already exists!")
        except IndexError:
            self.players.append(player)
            self.count += 1

    def remove(self, player):
        if player == "":
            raise ValueError("Player cannot be an empty string!")
        else:
            try:
                pl = [p for p in self.players if p.username == player][0]
                self.players.remove(pl)
                self.count -= 1
            except IndexError:                                          # better ??
                pass

    def find(self, player):
        pl = [p for p in self.players if p.username == player][0]
        return pl                                                       # or player object ??