from PyQt5 import QtGui

from structures.Drawable import Drawable


class Point(Drawable):
    def __init__(self, x: float, y: float, name: str = None):
        super().__init__(name)
        self.__x = x
        self.__y = y

    def draw(self, painter: QtGui.QPainter) -> None:
        painter.drawEllipse(self.__x, self.__y, 5, 5)

    def getX(self) -> float:
        return self.__x

    def getY(self) -> float:
        return self.__y

    def __str__(self) -> str:
        return f"{self.getName()}: ({self.getX()}, {self.getY()})"

    def getCoordinates(self) -> list:
        return [self.getX(), self.getY()]
