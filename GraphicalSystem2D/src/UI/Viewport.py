from PyQt5 import QtCore, QtGui, QtWidgets

from structures.Point import Point
from DisplayFile import displayFile

from utils.viewportTransformation import transformToWorldCoordinates


class Viewport(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Viewport, self).__init__(parent)
        self.setMouseTracking(True)
        self.__currentColor = QtCore.Qt.red
        self.currentSelectedType = ""

    def mousePressEvent(self, event):
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
        else:
            print("select a type first")

        self.update()

    def paintEvent(self, ev):
        qp = QtGui.QPainter(self)
        qp.setRenderHint(QtGui.QPainter.Antialiasing)

        brush = QtGui.QBrush(self.__currentColor)
        qp.setPen(self.__currentColor)
        qp.setBrush(brush)

        for point in displayFile.getPoints():
            normal_x, normal_y = displayFile.calculateNormalizedCoordinates(point)
            point.setNormalCoordinates(normal_x, normal_y)
            qp.setPen(QtGui.QPen(point.getColor(), 3))
            point.draw(qp)

        if displayFile.getBuffer() is not None:
            if not isinstance(displayFile.getBuffer(), Point):
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
            qp.setPen(QtGui.QPen(self.__currentColor, 3))
            displayFile.getBuffer().draw(qp)

        for line in displayFile.getLines():
            for point in line.getPoints():
                normal_x, normal_y = displayFile.calculateNormalizedCoordinates(point)
                point.setNormalCoordinates(normal_x, normal_y)

            qp.setPen(QtGui.QPen(line.getColor(), 3))
            line.draw(qp)

        for wireframe in displayFile.getWireframes():
            for point in wireframe.getPoints():
                normal_x, normal_y = displayFile.calculateNormalizedCoordinates(point)
                point.setNormalCoordinates(normal_x, normal_y)

            qp.setPen(QtGui.QPen(wireframe.getColor(), 3))
            wireframe.draw(qp)

    def getCurrentColor(self) -> None:
        return self.__currentColor

    def setCurrentColor(self, color) -> None:
        self.__currentColor = color
