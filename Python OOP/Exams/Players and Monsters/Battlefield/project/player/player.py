from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, username, health):
        self.username = username
        self.health = health
        self.card_repository: CardRepository
        self.is_dead = False

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value
        if self._username == "":
            raise ValueError("Player\'s username cannot be an empty string. ")

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = value
        if self._health <= 0:
            self._is_dead = True
            raise ValueError("Player's health bonus cannot be less than zero.")

    @property
    def is_dead(self):
        return self._is_dead

    @is_dead.setter
    def is_dead(self, value):
        self._is_dead = value
