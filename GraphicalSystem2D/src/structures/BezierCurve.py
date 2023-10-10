import numpy as np

from PyQt5.QtGui import QColor, QPainter

from structures.Drawable import Drawable
from structures.Point import Point

from utils.viewportTransformation import viewportTransformation
from utils.bezierUtils import getGBBezier, blendingFunction


class BezierCurve(Drawable):
    def __init__(
        self, name: str, coordinates: list[Point], color: QColor = None, window=None
    ):
        super().__init__(name)

        if len(coordinates) < 4:
            print("Invalid number of points for Bezier Curve")

        if (len(coordinates) - 4) % 3 != 0:
            print("Invalid number of points for Bezier Curve")

        self.__coordinates = coordinates
        self.__original_coordinates = coordinates
        self.__window = window

        if color is not None:
            self.__color = QColor(0, 0, 0)
        else:
            self.__color = color

        self.__curve_points = []

    def getCoordinates(self) -> list[Point]:
        return self.__coordinates

    def setCoordinates(self, coordinates: list[Point]) -> None:
        self.__coordinates = coordinates

    def getColor(self) -> QColor:
        return self.__color

    def setColor(self, color: str) -> None:
        self.__color = color

    def draw(self, painter: QPainter) -> None:
        acc = 0.001
        for i in range(0, len(self.__coordinates) - 3, 3):
            gb = getGBBezier(
                self.__coordinates[i],
                self.__coordinates[i + 1],
                self.__coordinates[i + 2],
                self.__coordinates[i + 3],
            )

            t = 0.0

            while t <= 1.0:
                x1 = blendingFunction(t, gb.x)
                y1 = blendingFunction(t, gb.y)
                x2 = blendingFunction(t + acc, gb.x)
                y2 = blendingFunction(t + acc, gb.y)

                self._drawLines(x1, y1, x2, y2, painter)  # change to normalized

                t += acc

                self.__curve_points.extend([Point(x1, y1), Point(x2, y2)])

    def _drawLines(self, x1, y1, x2, y2, painter):
        if x1 is not None and y1 is not None and x2 is not None and y2 is not None:
            x1, y1 = self.normalize(x1, y1)
            x1, y1 = viewportTransformation(x1, y1, self.__window)
            x2, y2 = self.normalize(x2, y2)
            x2, y2 = viewportTransformation(x2, y2, self.__window)
            painter.drawLine(x1, y1, x2, y2)

    def normalize(self, x, y):
        yw_min, yw_max, xw_min, xw_max = self.__window.getMinsAndMaxes()
        normal_x = (x - xw_min) / (xw_max - xw_min) * 2 - 1
        normal_y = (y - yw_min) / (yw_max - yw_min) * 2 - 1
        return (normal_x, normal_y)

    def applyTransformations(self, matrix: np.matrix) -> None:
        for point in self.__coordinates:
            mult = np.matmul(np.array([point.getX(), point.getY(), 1]), matrix)
            point.setX(mult.item(0))
            point.setY(mult.item(1))

    def calculateGeometricCenter(self) -> list:
        sum_x = 0
        sum_y = 0
        for point in self.__coordinates:
            sum_x += point.getX()
            sum_y += point.getY()

        return [sum_x / len(self.__coordinates), sum_y / len(self.__coordinates)]

    def reset(self) -> None:
        for point in self.__coordinates:
            point.reset()
