from PyQt5 import QtGui

from structures.Drawable import Drawable

from utils.viewportTransformation import viewportTransformation


class Point(Drawable):
    def __init__(self, x: float, y: float, window, name: str = None):
        super().__init__(name)
        self.__window = window
        self.__x = x
        self.__y = y

    def draw(self, painter: QtGui.QPainter) -> None:
        x, y = viewportTransformation(self.__x, self.__y, self.__window)
        painter.drawEllipse(x, y, 5, 5)
        
    def applyTransformations(self) -> None:
        pass

    def getX(self) -> float:
        return self.__x

    def getY(self) -> float:
        return self.__y

    def __str__(self) -> str:
        return f"{self.getName()}: ({self.getX()}, {self.getY()})"

    def getCoordinates(self) -> list:
        return [self.getX(), self.getY()]
