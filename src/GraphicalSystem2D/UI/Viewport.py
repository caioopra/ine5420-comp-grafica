from PyQt5 import QtCore, QtGui, QtWidgets

from structures.Point import Point
from structures.Line import Line
from DisplayFile import displayFile


class Viewport(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Viewport, self).__init__(parent)
        self.setMouseTracking(True)

        self.currentSelectedType = ""

    def mousePressEvent(self, event):
        if self.currentSelectedType == "POINT":
            displayFile.addToBuffer("POINT", Point(event.x(), event.y()))
        elif self.currentSelectedType == "LINE":
            displayFile.addToBuffer("LINE", Point(event.x(), event.y()))
        elif self.currentSelectedType == "WIREFRAME":
            displayFile.addToBuffer("WIREFRAME", Point(event.x(), event.y()))
        else:
            print("select a type first")

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