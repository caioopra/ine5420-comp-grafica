from PyQt5 import QtGui, QtCore

from structures.Drawable import Drawable
from structures.Line import Line
from structures.Point import Point


# class Wireframe(Drawable):
#     def __init__(self, pointA: Point, name: str = None):
#         super().__init__(name)
#         self.__currentLine = Line(pointA)
#         self.__linesList = []

#         self.__firstPoint = pointA
#         self.__lastPoint = None

#     def draw(self, painter: QtGui.QPainter):
#         painter.setPen(QtGui.QPen(QtCore.Qt.blue, 3))
#         painter.setBrush(QtGui.QBrush(QtCore.Qt.blue))
#         for line in self.__linesList:
#             line.draw(painter, wireframe=True)

#         for point in self.__currentLine.getPoints():
#             if point is not None:
#                 point.draw(painter)
                
#         self.__currentLine.draw(painter)

#     def addLine(self):
#         self.__linesList.append(self.__currentLine)
#         print(self.__linesList)
        
#     def getCurrentLine(self):
#         return self.__currentLine

#     # def addPoint(self, point: Point):
#     #     if self.__currentLine.getPointA() is self.__firstPoint:
#     #         self.__currentLine.addPoint(point)
#     #         self.addLine()
#     #         self.__currentLine = Line(point)
#     #     else:
#     #         # if self.__linesList[-1].getPointA() is not self.__firstPoint:
#     #         if len(self.__linesList) > 2:
#     #             self.__linesList.pop()
#     #         self.__currentLine.addPoint(point)
#     #         self.addLine()
#     #         self.__currentLine = Line(point, self.__firstPoint)
#     #         self.addLine()
#     #         print(self.__linesList)
#     #         # self.addLine()
#     #             # self.__linesList.pop()
            
#     #     # self.__currentLine.addPoint(point)
#     #     # self.addLine()
#     #     # self.__currentLine = Line(point)
        

            
                
                

#     def removeLastLine(self):
#         # x, y = self.__linesList[-1].getPointB().getCoordinates()
#         # if (
#         #     abs(x - self.__firstPoint.getX()) < 5
#         #     and abs(y - self.__firstPoint.getY()) < 5
#         # ):
#         #     self.__linesList[-1].setPointB(self.__firstPoint)
#         self.addLine()
#         self.__currentLine.clearPoints()

class Wireframe(Drawable):
    def __init__(self, pointA: Point, name: str = None):
        super().__init__(name)
        self.__firstPoint = pointA
        self.__pointsList = [pointA]

    def draw(self, painter: QtGui.QPainter):
        painter.setPen(QtGui.QPen(QtCore.Qt.blue, 3))
        painter.setBrush(QtGui.QBrush(QtCore.Qt.blue))
        
        if len(self.__pointsList) > 1:
            for i in range(len(self.__pointsList)):
                if i == len(self.__pointsList) - 1:
                    line = Line(self.__pointsList[i], self.__firstPoint)
                else:
                    line = Line(self.__pointsList[i], self.__pointsList[i+1])
                line.draw(painter, wireframe=True)
        else:
            self.__firstPoint.draw(painter)
    
    def addPoint(self, point: Point):
        self.__pointsList.append(point)
