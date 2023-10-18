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

    # TODO: FIX
    def applyTransformations(self, matrix: list) -> None:
        return super().applyTransformations(matrix)

    # TODO: FIX
    def calculateGeometricCenter(self) -> list:
        return super().calculateGeometricCenter()

    # TODO: FIX
    def reset(self) -> None:
        self.__coordinates = self.__original_coordinates
