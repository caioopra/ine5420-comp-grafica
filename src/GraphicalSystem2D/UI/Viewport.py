from PyQt5 import QtCore, QtGui, QtWidgets


class Viewport(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Viewport, self).__init__(parent)
        self.setMouseTracking(True)
        self.__points = []
        self.__lines = []
        self.__line_location = []
        self.current_event = ""

    def mouseMoveEvent(self, e):
        print(e.x(), e.y())

    def mousePressEvent(self, e):
        if self.current_event == "point":
            self.__points.append(e.pos())
        if self.current_event == "line":
            pass
        self.update()
        print(self.current_event)

    def paintEvent(self, ev):
        qp = QtGui.QPainter(self)
        qp.setRenderHint(QtGui.QPainter.Antialiasing)
        pen = QtGui.QPen(QtCore.Qt.red, 3)
        brush = QtGui.QBrush(QtCore.Qt.red)
        qp.setPen(pen)
        qp.setBrush(brush)
        for point in (self.__points):
            qp.drawEllipse(point, 5, 5)
