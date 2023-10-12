from PyQt5 import QtCore, QtGui, QtWidgets

from structures.Point import Point
from DisplayFile import displayFile

from structures.Wireframe import Wireframe
from utils.viewportTransformation import transformToWorldCoordinates
from utils.clipping.clipping import clip


class Viewport(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Viewport, self).__init__(parent)
        self.setMouseTracking(True)
        self.__currentColor = QtCore.Qt.red
        self.currentSelectedType = ""
        self.currentClippingMethod = ""

    def mousePressEvent(self, event):
        print("Current type: ", self.currentSelectedType)
        x, y = transformToWorldCoordinates(
            event.x(), event.y(), displayFile.getWindow()
        )
        if self.currentSelectedType != "":
            point = Point(x, y, displayFile.getWindow())
            normal_x, normal_y = displayFile.calculateNormalizedCoordinates(point)
            point.setNormalCoordinates(normal_x, normal_y)

        if self.currentSelectedType == "POINT":
            displayFile.addToBuffer(
                "POINT",
                point,
            )

        elif self.currentSelectedType == "LINE":
            displayFile.addToBuffer(
                "LINE",
                point,
            )
        elif self.currentSelectedType == "WIREFRAME":
            displayFile.addToBuffer(
                "WIREFRAME",
                point,
            )
        elif self.currentSelectedType == "CURVE":
            displayFile.addToBuffer(
                "CURVE",
                point,
            )
        else:
            print("select a type first")

        self.update()

    def paintEvent(self, ev):
        qp = QtGui.QPainter(self)
        qp.setRenderHint(QtGui.QPainter.Antialiasing)

        brush = QtGui.QBrush(self.__currentColor)
        brush.setStyle(QtCore.Qt.SolidPattern)
        qp.setPen(self.__currentColor)
        qp.setBrush(brush)
        
        if displayFile.getBuffer() is not None:
            if isinstance(displayFile.getBuffer(), list):
                for point in displayFile.getBuffer():
                    normal_x, normal_y = displayFile.calculateNormalizedCoordinates(
                        point
                    )
                    point.setNormalCoordinates(normal_x, normal_y)
                
            elif not isinstance(displayFile.getBuffer(), Point):
                points = displayFile.getBuffer().getPoints()
                for point in points:
                    if point is not None:
                        normal_x, normal_y = displayFile.calculateNormalizedCoordinates(
                            point
                        )
                        point.setNormalCoordinates(normal_x, normal_y)
            else:
                normal_x, normal_y = displayFile.calculateNormalizedCoordinates(
                    displayFile.getBuffer()
                )
                displayFile.getBuffer().setNormalCoordinates(normal_x, normal_y)
                
        for point in displayFile.getPoints():
            normal_x, normal_y = displayFile.calculateNormalizedCoordinates(point)
            point.setNormalCoordinates(normal_x, normal_y)

        for line in displayFile.getLines():
            for point in line.getPoints():
                normal_x, normal_y = displayFile.calculateNormalizedCoordinates(point)
                point.setNormalCoordinates(normal_x, normal_y)

        for wireframe in displayFile.getWireframes():
            for point in wireframe.getPoints():
                normal_x, normal_y = displayFile.calculateNormalizedCoordinates(point)
                point.setNormalCoordinates(normal_x, normal_y)

        to_draw_objects = clip(self.currentClippingMethod)
        print("\nwill draw:", to_draw_objects)
        for obj in to_draw_objects:
            if obj is displayFile.getBuffer():
                pen = QtGui.QPen(self.__currentColor, 3)
                qp.setPen(pen)
            else:
                pen = QtGui.QPen(obj.getColor(), 3)
                qp.setPen(pen)
            brush.setStyle(QtCore.Qt.SolidPattern)
            if isinstance(obj, Wireframe):
                if obj.getIsFilled():
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    qp.setBrush(brush)
                else:
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    qp.setBrush(brush)
            obj.draw(qp)

    def getCurrentColor(self) -> None:
        return self.__currentColor

    def setCurrentColor(self, color) -> None:
        self.__currentColor = color

    def setCurrentClippingMethod(self, type: str) -> None:
        self.currentClippingMethod = type
        self.update()
