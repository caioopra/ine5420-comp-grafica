from PyQt5 import QtGui, QtCore

from structures.Drawable import Drawable
from structures.Line import Line
from structures.Point import Point


class Wireframe(Drawable):
    def __init__(self, pointA: Point, name: str = None):
        super().__init__(name)
        self.__firstPoint = pointA
        self.__pointsList = [pointA]

    def draw(self, painter: QtGui.QPainter):
        painter.setPen(QtGui.QPen(QtCore.Qt.blue, 3))
        painter.setBrush(QtGui.QBrush(QtCore.Qt.blue))

        if len(self.__pointsList) > 1:
            for i in range(len(self.__pointsList)):
                if i == len(self.__pointsList) - 1:
                    line = Line(self.__pointsList[i], self.__firstPoint)
                else:
                    line = Line(self.__pointsList[i], self.__pointsList[i + 1])
                line.draw(painter, wireframe=True)
        else:
            self.__firstPoint.draw(painter)

    def addPoint(self, point: Point):
        self.__pointsList.append(point)
