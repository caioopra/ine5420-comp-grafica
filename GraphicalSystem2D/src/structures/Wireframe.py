from PyQt5 import QtGui, QtCore
import numpy as np

from structures.Drawable import Drawable
from structures.Line import Line
from structures.Point import Point


class Wireframe(Drawable):
    def __init__(self, pointA: Point, name: str = None, window=None):
        super().__init__(name)
        self.__firstPoint = pointA
        self.__pointsList = [pointA]
        self.__window = window

    def draw(self, painter: QtGui.QPainter):
        if len(self.__pointsList) > 1:
            for i in range(len(self.__pointsList)):
                if i == len(self.__pointsList) - 1:
                    line = Line(
                        self.__pointsList[i], self.__firstPoint, window=self.__window
                    )
                else:
                    line = Line(
                        self.__pointsList[i],
                        self.__pointsList[i + 1],
                        window=self.__window,
                    )
                line.draw(painter, wireframe=True)
        else:
            self.__firstPoint.draw(painter)

    def applyTransformations(self, matrix: np.matrix) -> None:
        for point in self.__pointsList:
            mult = np.matmul(np.array([point.getX(), point.getY(), 1]), matrix)
            point.setX(mult.item(0))
            point.setY(mult.item(1))

    def calculateGeometricCenter(self) -> list:
        xSum = 0
        ySum = 0
        for point in self.__pointsList:
            xSum += point.getX()
            ySum += point.getY()

        return [xSum / len(self.__pointsList), ySum / len(self.__pointsList)]

    def reset(self) -> None:
        for point in self.__pointsList:
            point.reset()

    def addPoint(self, point: Point):
        self.__pointsList.append(point)
