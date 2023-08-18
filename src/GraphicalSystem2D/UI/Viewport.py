from PyQt5 import QtCore, QtGui, QtWidgets


class Viewport(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Viewport, self).__init__(parent)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, e):
        print(e.x(), e.y())
