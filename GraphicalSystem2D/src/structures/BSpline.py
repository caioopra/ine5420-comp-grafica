from PyQt5.QtGui import QColor, QPainter
import numpy as np

from structures.Drawable import Drawable
from structures.Point import Point

from utils.bSplineUtils import (
    calculateDeltaMatrix,
    getGBSpline,
    getInitialCurve,
    forward_difference,
)



class BSpline(Drawable):
    def __init__(
        self, name: str, coordinates: list[Point], color: QColor = None, window=None
    ):
        super().__init__(name)

        if len(coordinates) < 4:
            print("Invalid number of points for BSpline curve")

        self.__coordinates = coordinates
        self.__original_coordinates = coordinates
        self.__window = window

        if color == None:
            self.__color = QColor(0, 0, 0)
        else:
            self.__color = color

    def draw(self, painter: QPainter) -> None:
        delta = 0.01
        n = 1 / delta
        delta_matrix = calculateDeltaMatrix(delta)

        for i in range(len(self.__coordinates) - 3):
            gb_spline = getGBSpline(
                self.__coordinates[i],
                self.__coordinates[i + 1],
                self.__coordinates[i + 2],
                self.__coordinates[i + 3],
            )

            dx, dy = getInitialCurve(delta_matrix, gb_spline)

            forward_difference(n, dx, dy, painter, self.__window)

    def applyTransformations(self, matrix: list) -> None:
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

    # TODO: FIX
    def reset(self) -> None:
        for p in self.__coordinates:
            p.reset()
