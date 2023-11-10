import numpy as np
from PyQt5 import QtGui

from structures.Drawable import Drawable

from utils.viewportTransformation import viewportTransformation
from utils.matrixOperations import parallel_projection


class Point(Drawable):
    def __init__(self, x: float, y: float, z: float = 0, window=None, name: str = None):
        super().__init__(name)
        self.__window = window

        self.__x = x
        self.__normal_x = x
        self.__original_x = x

        self.__y = y
        self.__normal_y = y
        self.__original_y = y

        self.__z = z
        self.__normal_z = z
        self.__original_z = z

    def draw(self, painter: QtGui.QPainter) -> None:
        print(self.__window)
        print(self.__window)
        projection = parallel_projection(self.__window)
        proj = np.dot(np.array([self.__x, self.__y, self.__z, 1]), projection)
        x, y = self.calculateNormalizedCoordinates(proj[0], proj[1])
        print("Calculated")
        # x, y = self.calculateNormalizedCoordinates(self.__x, self.__y)
        x, y = viewportTransformation(x, y, self.__window)
        painter.drawEllipse(x, y, 5, 5)

    def applyTransformations(self, matrix: np.matrix) -> None:
        mult = np.matmul(np.array([self.__x, self.__y, self.__z, 1]), matrix)
        self.__x = mult.item(0)
        self.__y = mult.item(1)
        self.__z = mult.item(2)

    def calculateGeometricCenter(self) -> list:
        return [self.getX(), self.getY(), self.getZ()]

    def calculateNormalizedCoordinates(self, x, y):
        yw_min, yw_max, xw_min, xw_max = self.__window.getMinsAndMaxes()
        normal_x = (x - xw_min) / (xw_max - xw_min) * 2 - 1
        normal_y = (y - yw_min) / (yw_max - yw_min) * 2 - 1

        return (normal_x, normal_y)

    def reset(self) -> None:
        self.__x = self.__original_x
        self.__y = self.__original_y
        self.__z = self.__original_z

    def getX(self) -> float:
        return self.__x

    def getY(self) -> float:
        return self.__y

    def getZ(self) -> float:
        return self.__z

    def setX(self, value: float) -> None:
        self.__x = value

    def setY(self, value: float) -> None:
        self.__y = value

    def setZ(self, value: float) -> None:
        self.__z = value
        
    def getWindow(self):
        return self.__window

    def setNormalCoordinates(
        self, value_x: float, value_y: float, value_z: float = 0
    ) -> None:
        self.__normal_x = value_x
        self.__normal_y = value_y
        self.__normal_z = value_z

    def __str__(self) -> str:
        return f"{self.getName()}: ({self.getX()}, {self.getY()}, {self.getZ()})"

    def getCoordinates(self) -> list:
        # return [self.getX(), self.getY(), self.getZ()]
        return [self.getX(), self.getY()]

    # TODO: remove this and use only getCoordinates
    def getAllCoordinates(self) -> list:
        return [self.getX(), self.getY(), self.getZ()]

    def getNormalX(self) -> float:
        return self.__normal_x

    def getNormalY(self) -> float:
        return self.__normal_y

    def getNormalZ(self) -> float:
        return self.__normal_z

    def getNormalCoordinates(self) -> list[int]:
        # return [self.__normal_x, self.__normal_y, self.__normal_z]
        return [self.__normal_x, self.__normal_y]

    def getPointAsVector(self) -> str:
        return f"v {self.__original_x} {self.__original_y} {self.__original_z}"

    def setWindow(self, window) -> None:
        self.__window = window

    def between(self, min: object, max: object) -> bool:
        if isinstance(min, Point) and isinstance(max, Point):
            x = max.getNormalX() > self.getNormalX() > min.getNormalX()
            y = max.getNormalY() > self.getNormalY() > min.getNormalY()

            return x and y

        return False
