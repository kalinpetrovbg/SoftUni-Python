from project.medicine.medicine import Medicine
from abc import ABC, abstractmethod
from project.survivor import Survivor


class Salve(Medicine, ABC):
    def __init__(self):
        super().__init__(health_increase=50)

    @property
    def health_increase(self):
        return self.__health_increase

    @abstractmethod
    def apply(self, survivor: Survivor):
        survivor.health += self.__health_increase
        if survivor.health > 100:
            survivor.health = 100
