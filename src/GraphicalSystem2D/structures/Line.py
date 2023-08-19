from PyQt5 import QtGui, QtCore

from structures.Drawable import Drawable
from structures.Point import Point


class Line(Drawable):
    def __init__(self, PointA: Point, PointB: Point = None, name: str = None):
        self.__pointA = PointA
        self.__pointB = PointB

    def draw(self, painter: QtGui.QPainter) -> None:
        painter.setPen(QtGui.QPen(QtCore.Qt.green, 3))
        painter.setBrush(QtGui.QBrush(QtCore.Qt.green))

        if self.__pointB is not None:
            painter.drawLine(
                self.__pointA.getX(),
                self.__pointA.getY(),
                self.__pointB.getX(),
                self.__pointB.getY(),
            )
            print("line being drawn")
        else:
            self.__pointA.draw(painter)

    def addPoint(self, point: Point):
        if self.__pointB is None:
            self.__pointB = point
        elif self.__pointB is not None:
            self.__pointA = self.__pointB
            self.__pointB = point

    def getPoints(self) -> list:
        """
        Returns a list with the two Point objects of the line
        """
        return [self.__pointA, self.__pointB]
