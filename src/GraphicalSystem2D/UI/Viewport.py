from PyQt5 import QtCore, QtGui, QtWidgets

from structures.Point import Point
from structures.Line import Line
from DisplayFile import displayFile

from utils.viewportTransformation import transformToWorldCoordinates


class Viewport(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Viewport, self).__init__(parent)
        self.setMouseTracking(True)

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
        pen = QtGui.QPen(QtCore.Qt.red, 3)
        brush = QtGui.QBrush(QtCore.Qt.red)
        qp.setPen(pen)
        qp.setBrush(brush)

        for point in displayFile.getPoints():
            point.draw(qp)

        if displayFile.getBuffer() is not None:
            displayFile.getBuffer().draw(qp)

        for line in displayFile.getLines():
            line.draw(qp)

        for wireframe in displayFile.getWireframes():
            wireframe.draw(qp)
