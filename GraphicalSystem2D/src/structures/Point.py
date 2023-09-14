import numpy as np
from PyQt5 import QtGui

from structures.Drawable import Drawable

from utils.viewportTransformation import viewportTransformation


class Point(Drawable):
    def __init__(self, x: float, y: float, window, name: str = None):
        super().__init__(name)
        self.__window = window
        self.__x = x
        self.__normal_x = x
        self.__original_x = x
        self.__y = y
        self.__normal_y = y
        self.__original_y = y

    def draw(self, painter: QtGui.QPainter) -> None:
        x, y = viewportTransformation(self.__x, self.__y, self.__window)
        painter.drawEllipse(x, y, 5, 5)

    def applyTransformations(self, matrix: np.matrix) -> None:
        mult = np.matmul(np.array([self.__x, self.__y, 1]), matrix)
        self.__x = mult.item(0)
        self.__y = mult.item(1)

    def calculateGeometricCenter(self) -> list:
        return [self.getX(), self.getY()]
    
    def reset(self) -> None:
        self.__x = self.__original_x
        self.__y = self.__original_y

    def getX(self) -> float:
        return self.__x

    def getY(self) -> float:
        return self.__y

    def setX(self, value: float) -> None:
        self.__x = value

    def setY(self, value: float) -> None:
        self.__y = value

    def setNormalCoordinates(self, value_x: float, value_y: float) -> None:
        self.__normal_x = value_x
        self.__normal_y = value_y

    def __str__(self) -> str:
        return f"{self.getName()}: ({self.getX()}, {self.getY()})"

    def getCoordinates(self) -> list:
        return [self.getX(), self.getY()]

    def getNormalX(self) -> float:
        return self.__normal_x
    
    def getNormalY(self) -> float:
        return self.__normal_y
