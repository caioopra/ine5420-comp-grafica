from structures.Point import Point
from structures.Line import Line
from structures.Drawable import Drawable
from PyQt5 import QtGui
from structures.Bicubic import getBicubicGB, blending_function_bicubic
from PyQt5.QtGui import QPainter, QPen
from collections import defaultdict
from PyQt5 import QtCore

class BezierBicubicSurface(Drawable):
    def __init__(
        self, points: [Point], name: str = None, window=None
    ):
        super().__init__(name)
        if len(points) == 16:
            self.__points = points
        self.__window = window

    def draw(self, painter: QPainter):
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(QtCore.Qt.black)
        painter.setPen(pen)

        gb = getBicubicGB(self.__points)
        
        points = defaultdict(list)
        accuracy = 0.111
        s = 0.0
        t = 0.0
        while s <= 1.0:
            t = 0.0
            while t <= 1.0:
                x1 = blending_function_bicubic(s, t, gb.x)
                y1 = blending_function_bicubic(s, t, gb.y)
                z1 = blending_function_bicubic(s, t, gb.z)
                points[s].append(Point(x1[0][0], y1[0][0], z1[0][0]))            
                t += accuracy
            s += accuracy    

        lines = []
        # Direção S
        for k, v in points.items():
            for i in range(len(v)-1):
                lines.append(Line(Point(v[i].getNormalX(), v[i].getNormalY(), v[i].getNormalZ()), Point(v[i+1].getNormalX(), v[i+1].getNormalY(), v[i+1].getNormalZ())))

        # Direção T
        for i in range(10):
            t_list = [elem[i] for elem in points.values()]
            for j in range(len(t_list)-1):
                lines.append(Line(Point(t_list[j].getNormalX(), t_list[j].getNormalY(), t_list[j].getNormalZ()), Point(t_list[j+1].getNormalX(), t_list[j+1].getNormalY(), t_list[j+1].getNormalZ())))
            
        for line in lines:
            line.draw(painter)

    def applyTransformations(self, matrix) -> None:
        pass

    def reset(self):
        pass

    def calculateGeometricCenter(self) -> list:
        return super().calculateGeometricCenter()

    def getWindow(self):
        return self.__window

    def setWindow(self, window):
        self.__window = window