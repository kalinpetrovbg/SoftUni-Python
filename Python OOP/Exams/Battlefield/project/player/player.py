from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, username, health):
        self.username = username
        self.health = health
        self.card_repository: CardRepository
        self.is_dead = False

    @property
    def username(self):
        self.username = self._username

    @username.setter
    def username(self, value):
        self._username = value
        if self._username == "":
            raise ValueError("Player\'s username cannot be an empty string. ")

    @property
    def health(self):
        self.health = self._health

    @health.setter
    def health(self, value):
        self._health = value
        if self._health <= 0:
            self._is_dead = True
            raise ValueError("Player's health bonus cannot be less than zero.")

    @property
    def is_dead(self):
        self._is_dead = self._is_dead
    
