from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPolygon
import numpy as np
from PyQt5.QtCore import QPoint

from structures.Drawable import Drawable
from structures.Line import Line
from structures.Point import Point
from utils.viewportTransformation import viewportTransformation


class Wire3D(Drawable):
    def __init__(
        self, lines:[Line], name: str = None, window=None
    ):
        super().__init__(name)
        self.__lines = lines
        self.__window = window

    def setWindow(self, window):
        self.__window = window

    def draw(self, painter: QtGui.QPainter):
        for line in self.__lines:
            line.draw(painter)
        '''for cloud in self.__clouds:
            if len(cloud) > 1:
                for i in range(len(cloud)):
                    if i == len(cloud) - 1:
                        line = Line(
                            cloud[i], cloud[0], window=self.__window
                        )
                    else:
                        line = Line(
                            cloud[i],
                            cloud[i + 1],
                            window=self.__window,
                        )
                    line.draw(painter, wireframe=True)
            else:
                print("obj:", cloud[0])
                cloud[0].draw(painter)'''

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
        for cloud in self.__clouds:
            for point in cloud:
                point.reset()

    def getClouds(self) -> list:
        return self.__clouds

    def setClouds(self, clouds) -> None:
        self.__clouds = clouds

    def getWindow(self):
        return self.__window
