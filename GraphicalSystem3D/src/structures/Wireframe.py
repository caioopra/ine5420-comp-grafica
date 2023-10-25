from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPolygon
import numpy as np
from PyQt5.QtCore import QPoint

from structures.Drawable import Drawable
from structures.Line import Line
from structures.Point import Point
from utils.viewportTransformation import viewportTransformation


class Wireframe(Drawable):
    def __init__(
        self, pointA: Point, name: str = None, window=None, is_filled: bool = False
    ):
        super().__init__(name)
        self.__firstPoint = pointA
        self.__pointsList = [pointA]
        self.__window = window
        self.__is_filled = is_filled

    def setWindow(self, window):
        self.__window = window

    def draw(self, painter: QtGui.QPainter):
        if self.__is_filled:
            points = []
            for point in self.__pointsList:
                x, y = viewportTransformation(point.getNormalX(), point.getNormalY(), self.__window)
                points.append(QPoint(x, y))
            #painter.setPen(self.__color)
            painter.drawPolygon(points)

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
            print("obj:", self.__firstPoint)
            self.__firstPoint.draw(painter)

    def applyTransformations(self, matrix: np.matrix) -> None:
        for point in self.__pointsList:
            mult = np.matmul(np.array([point.getX(), point.getY(), 1]), matrix)
            point.setX(mult.item(0))
            point.setY(mult.item(1))

    def calculateGeometricCenter(self) -> list:
        xSum = 0
        ySum = 0
        zSum = 0
        for point in self.__pointsList:
            xSum += point.getX()
            ySum += point.getY()
            zSum += point.getZ()

        return [xSum / len(self.__pointsList), ySum / len(self.__pointsList)]

    def reset(self) -> None:
        for point in self.__pointsList:
            point.reset()

    def addPoint(self, point: Point):
        self.__pointsList.append(point)

    def getPoints(self) -> list:
        return self.__pointsList

    def getIsFilled(self) -> bool:
        return self.__is_filled

    def setPoints(self, points) -> None:
        self.__pointsList = points

    def setIsFilled(self, status: bool) -> None:
        self.__is_filled = status

    def getWindow(self):
        return self.__window

    def fill(self):
        if self.__is_filled:
            self.__is_filled = False
        else:
            self.__is_filled = True
