from abc import ABC, abstractmethod


class Drawable(ABC):
    def __init__(self) -> None:
        self.__name = ""

    @abstractmethod
    def draw(self):
        pass

    def setName(self, name: str) -> None:
        self.__name = name
        
    def getName(self) -> str:
        return self.__name