from PyQt5 import QtGui
import numpy as np

from structures.Drawable import Drawable
from structures.Point import Point

from utils.viewportTransformation import viewportTransformation


class Line(Drawable):
    def __init__(
        self, pointA: Point, pointB: Point = None, name: str = None, window=None
    ):
        super().__init__(name)
        self.__window = window
        self.__pointA = pointA
        self.__pointB = pointB

    def draw(self, painter: QtGui.QPainter, wireframe: bool = False) -> None:
        if self.__pointB is not None:
            pointA_x, pointA_y = viewportTransformation(
                self.__pointA.getNormalX(), self.__pointA.getNormalY(), self.__window
            )
            pointB_x, pointB_y = viewportTransformation(
                self.__pointB.getNormalX(), self.__pointB.getNormalY(), self.__window
            )
            painter.drawLine(pointA_x, pointA_y, pointB_x, pointB_y)
        else:
            self.__pointA.draw(painter)

    def applyTransformations(self, matrix) -> None:
        mult = np.matmul(
            np.array([self.__pointA.getX(), self.__pointA.getY(), 1]), matrix
        )
        self.__pointA.setX(mult.item(0))
        self.__pointA.setY(mult.item(1))
        mult = np.matmul(
            np.array([self.__pointB.getX(), self.__pointB.getY(), 1]), matrix
        )
        self.__pointB.setX(mult.item(0))
        self.__pointB.setY(mult.item(1))

    def calculateGeometricCenter(self) -> list:
        somaX = (self.__pointA.getX() + self.__pointB.getX()) / 2
        somaY = (self.__pointA.getY() + self.__pointB.getY()) / 2

        return [somaX, somaY]

    def reset(self) -> None:
        self.__pointA.reset()
        self.__pointB.reset()

    def addPoint(self, point: Point):
        if self.__pointB is None:
            self.__pointB = point
        elif self.__pointB is not None:
            self.__pointA = self.__pointB
            self.__pointB = point

    def setWindow(self, window):
        self.__window = window

    def getPoints(self) -> list[Point]:
        """
        Returns a list with the two Point objects of the line
        """
        return [self.__pointA, self.__pointB]
    
    def setCoordinates(self, pointA: Point, pointB: Point) -> None:
        self.__pointA = pointA
        self.__pointB = pointB

    def setNormalCoordinates(self, pointA: Point, pointB: Point) -> None:
        self.__pointA = pointA
        self.__pointB = pointB
