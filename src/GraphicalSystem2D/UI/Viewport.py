from PyQt5 import QtCore, QtGui, QtWidgets

from structures.Point import Point
from DisplayFile import displayFile


class Viewport(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Viewport, self).__init__(parent)
        self.setMouseTracking(True)
        self.__buffer = None

        self.__points = []
        self.__lines = []
        self.__polygons = []

        self.currentTypeSelected = ""

    def mouseMoveEvent(self, e):
        print(e.x(), e.y())

    def mousePressEvent(self, event):
        if self.currentTypeSelected == "POINT":
            displayFile.setBuffer(Point(event.x(), event.y()))

            self.__points.append(event.pos())
        elif self.currentTypeSelected == "LINE":
            pass
        elif self.currentTypeSelected == "POLYGON":
            ...

        self.update()
        print(self.currentTypeSelected)

    def registerObject(self, objectName: str) -> None:
        nameIsValid = displayFile.verifyIfNameIsValid(objectName)
        if nameIsValid:
            displayFile.registerObject(self.currentTypeSelected)

    def paintEvent(self, ev):
        qp = QtGui.QPainter(self)
        qp.setRenderHint(QtGui.QPainter.Antialiasing)
        pen = QtGui.QPen(QtCore.Qt.red, 3)
        brush = QtGui.QBrush(QtCore.Qt.red)
        qp.setPen(pen)
        qp.setBrush(brush)
        for point in self.__points:
            print(point)
            qp.drawEllipse(point, 5, 5)
    
    # def paintEvent(self, ev):
    #     qp = QtGui.QPainter(self)
    #     qp.setRenderHint(QtGui.QPainter.Antialiasing)
    #     pen = QtGui.QPen(QtCore.Qt.red, 3)
    #     brush = QtGui.QBrush(QtCore.Qt.red)
    #     qp.setPen(pen)
    #     qp.setBrush(brush)
    #     for point in displayFile.getPoints():
    #         print("point", point)
    #         qp.drawEllipse(point, 5, 5)
        
        # if displayFile.getBuffer() is not None:
        #     qp.drawEllipse(displayFile.getBuffer(), 5, 5)
