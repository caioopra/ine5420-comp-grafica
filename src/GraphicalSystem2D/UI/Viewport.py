from PyQt5 import QtCore, QtGui, QtWidgets


class Viewport(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Viewport, self).__init__(parent)
        self.setMouseTracking(True)
        self.__points = QtGui.QPolygon()

    def mouseMoveEvent(self, e):
        print(e.x(), e.y())

    def mousePressEvent(self, e):
        self.__points << e.pos()
        self.update()
        print("a")

    def paintEvent(self, ev):
        qp = QtGui.QPainter(self)
        qp.setRenderHint(QtGui.QPainter.Antialiasing)
        pen = QtGui.QPen(QtCore.Qt.red, 3)
        brush = QtGui.QBrush(QtCore.Qt.red)
        qp.setPen(pen)
        qp.setBrush(brush)
        for i in range(self.__points.count()):
            qp.drawEllipse(self.__points.point(i), 5, 5)