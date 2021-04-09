from project.player.player import Player


class Advanced(Player):
    def __init__(self, username):
        super().__init__(username, health=250)

a = Advanced("Petrov")

print(a.username)
print(a.health)