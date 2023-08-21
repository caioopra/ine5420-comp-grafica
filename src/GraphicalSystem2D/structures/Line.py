from PyQt5 import QtGui, QtCore

from structures.Drawable import Drawable
from structures.Point import Point

from utils.viewportTransformation import (
    viewportTransformation,
    transformToWorldCoordinates,
)


class Line(Drawable):
    def __init__(
        self, pointA: Point, pointB: Point = None, name: str = None, window=None
    ):
        super().__init__(name)
        self.__window = window
        self.__pointA = self.createPoint(
            (pointA.getX(), pointA.getY(), self.__window)
        )

        if pointB is not None:
            self.__pointB = self.createPoint(
                (pointB.getX(), pointB.getY(), self.__window)
            )
        else:
            self.__pointB = pointB

    def draw(self, painter: QtGui.QPainter, wireframe: bool = False) -> None:
        if not wireframe:
            painter.setPen(QtGui.QPen(QtCore.Qt.green, 3))
            painter.setBrush(QtGui.QBrush(QtCore.Qt.green))

        if self.__pointB is not None:
            pointA_x, pointA_y = viewportTransformation(
                self.__pointA.getX(), self.__pointA.getY(), self.__window
            )
            pointB_x, pointB_y = viewportTransformation(
                self.__pointB.getX(), self.__pointB.getY(), self.__window
            )
            painter.drawLine(pointA_x, pointA_y, pointB_x, pointB_y)
        else:
            self.__pointA.draw(painter)

    def createPoint(self, points):
        return Point(points[0], points[1], self.__window)

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
