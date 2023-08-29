from abc import ABC, abstractmethod

import numpy as np

from PyQt5 import QtCore

class Drawable(ABC):
    def __init__(self, name: str = None) -> None:
        self.__name = name
        self.__current_transformations = None  # np.matrix
        self.__color = QtCore.Qt.red

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def applyTransformations(self, matrix: np.matrix) -> None:
        pass
    
    @abstractmethod
    def calculateGeometricCenter(self) -> list:
        pass

    def setName(self, name: str) -> None:
        self.__name = name

    def getName(self) -> str:
        return self.__name

    def getCurrentTransformations(self) -> np.matrix | None:
        return self.__current_transformations

    def setCurrentTransformations(self, transformations: np.matrix) -> None:
        self.__current_transformations = transformations

    def getColor(self) -> str:
        return self.__color

    def setColor(self, color: str) -> None:
        self.__color = color
        