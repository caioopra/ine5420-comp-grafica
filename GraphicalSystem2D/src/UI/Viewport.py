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

        if self.currentSelectedType == "POINT":
            displayFile.addToBuffer(
                "POINT",
                Point(
                    x,
                    y,
                    displayFile.getWindow(),
                ),
            )

        elif self.currentSelectedType == "LINE":
            displayFile.addToBuffer(
                "LINE",
                Point(
                    x,
                    y,
                    displayFile.getWindow(),
                ),
            )
        elif self.currentSelectedType == "WIREFRAME":
            displayFile.addToBuffer(
                "WIREFRAME",
                Point(
                    x,
                    y,
                    displayFile.getWindow(),
                ),
            )
        else:
            print("select a type first")  # TODO: add to log

        self.update()

    def paintEvent(self, ev):
        qp = QtGui.QPainter(self)
        qp.setRenderHint(QtGui.QPainter.Antialiasing)

        brush = QtGui.QBrush(self.__currentColor)
        qp.setPen(self.__currentColor)
        qp.setBrush(brush)

        for point in displayFile.getPoints():
            qp.setPen(QtGui.QPen(point.getColor(), 3))
            point.draw(qp)

        if displayFile.getBuffer() is not None:
            qp.setPen(QtGui.QPen(self.__currentColor, 3))
            displayFile.getBuffer().draw(qp)

        for line in displayFile.getLines():
            qp.setPen(QtGui.QPen(line.getColor(), 3))
            line.draw(qp)

        for wireframe in displayFile.getWireframes():
            qp.setPen(QtGui.QPen(wireframe.getColor(), 3))
            wireframe.draw(qp)

    def getCurrentColor(self) -> None:
        return self.__currentColor

    def setCurrentColor(self, color) -> None:
        self.__currentColor = color
