from PyQt5 import QtGui

from structures.Drawable import Drawable


class Point(Drawable):
    def __init__(self, x: float, y: float, name: str = None):
        self.__x = x
        self.__y = y
        self.__name = name

    def draw(self, painter: QtGui.QPainter) -> None:
        painter.drawEllipse(self.__x, self.__y, 5, 5)
        print("point drawing itself")

    def getX(self) -> float:
        return self.__x

    def getY(self) -> float:
        return self.__y

    def getName(self) -> str:
        return self.__name

    def __str__(self) -> str:
        return f"{self.getName()}: ({self.getX()}, {self.getY()})"

    def getCoordinates(self) -> tuple:
        return (self.getX(), self.getY())
