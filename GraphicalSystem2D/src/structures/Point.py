from PyQt5 import QtGui

from structures.Drawable import Drawable

from utils.viewportTransformation import viewportTransformation


class Point(Drawable):
    def __init__(self, x: float, y: float, window, name: str = None):
        super().__init__(name)
        self.__window = window
        self.__x = x
        self.__original_x = x
        self.__y = y
        self.__original_y = y

    def draw(self, painter: QtGui.QPainter) -> None:
        x, y = viewportTransformation(self.__x, self.__y, self.__window)
        painter.drawEllipse(x, y, 5, 5)

    def applyTransformations(self) -> None:
        pass

    def calculateGeometricCenter(self) -> list:
        return [self.getX(), self.getY()]

    def getX(self) -> float:
        return self.__x

    def getY(self) -> float:
        return self.__y

    def setX(self, value: float) -> None:
        self.__x = value

    def setY(self, value: float) -> None:
        self.__y = value

    def getOriginalX(self) -> float:
        return self.__original_x

    def getOriginalY(self) -> float:
        return self.__original_y

    def __str__(self) -> str:
        return f"{self.getName()}: ({self.getX()}, {self.getY()})"

    def getCoordinates(self) -> list:
        return [self.getX(), self.getY()]
