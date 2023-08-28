from abc import ABC, abstractmethod

import numpy as np


class Drawable(ABC):
    def __init__(self, name: str = None) -> None:
        self.__name = name
        self.__current_transformations = None  # np.matrix

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def applyTransformations(self) -> None:
        pass

    def setName(self, name: str) -> None:
        self.__name = name

    def getName(self) -> str:
        return self.__name

    def getCurrentTransformations(self) -> np.matrix | None:
        return self.__current_transformations

    def setCurrentTransformations(self, transformations: np.matrix) -> None:
        self.__current_transformations = transformations
