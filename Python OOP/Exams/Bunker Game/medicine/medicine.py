from abc import ABC, abstractmethod
from project.survivor import Survivor


class Medicine(ABC):
    def __init__(self, health_increase):
        self.__health_increase = health_increase
        if self.__health_increase < 0:
            raise ValueError("Health increase cannot be less than zero.")

    @property
    def health_increase(self):
        return self.__health_increase

    @abstractmethod
    def apply(self, survivor: Survivor):
        survivor.health += self.__health_increase
        if survivor.health > 100:
            survivor.health = 100
