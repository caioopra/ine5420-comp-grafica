from abc import ABC, abstractmethod


class Drawable(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def draw(self):
        pass

