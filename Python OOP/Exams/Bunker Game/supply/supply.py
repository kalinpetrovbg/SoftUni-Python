from abc import ABC, abstractmethod
from project.survivor import Survivor


class Supply(ABC):
    def __init__(self, needs_increase):
        self.__needs_increase = needs_increase

    @property
    def needs_increase(self):
        return self.__needs_increase

    @abstractmethod
    def apply(self, survivor: Survivor):
        survivor.needs += self.__needs_increase
        if survivor.needs > 100:
            survivor.needs = 100