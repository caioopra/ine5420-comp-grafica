from PyQt5 import QtGui, QtCore

from structures.Drawable import Drawable
from structures.Line import Line
from structures.Point import Point

class Wireframe(Drawable):
    def __init__(self, pointA: Point, name: str = None):
        super().__init__(name)
        self.__currentLine = Line(pointA)
        self.__linesList = []
    
    def draw(self, painter: QtGui.QPainter):
        painter.setPen(QtGui.QPen(QtCore.Qt.blue, 3))
        painter.setBrush(QtGui.QBrush(QtCore.Qt.blue))
        for line in self.__linesList:
            line.draw(painter, wireframe=True)
            
        for point in self.__currentLine.getPoints():
            if point is not None:
                point.draw(painter)
    
    def addLine(self):
        self.__linesList.append(self.__currentLine)
    
    def addPoint(self, point: Point):
        if self.__currentLine is None:
            self.__currentLine = Line(point)
        elif self.__currentLine.getPointB() is None:
            self.__currentLine.addPoint(point)
            self.addLine()
            self.__currentLine = Line(point)

    def removeLastLine(self):
        self.__currentLine.clearPoints()