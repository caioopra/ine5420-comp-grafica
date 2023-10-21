from PyQt5 import QtCore, QtGui, QtWidgets


class Object3DCreationModal(object):
    def setupUi(
        self, MainWindow, closeModal
    ):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 250)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(11)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # ==========================
        # ======== X INPUT =========
        self.translationXInput = QtWidgets.QLabel(self.centralwidget)
        self.translationXInput.setGeometry(QtCore.QRect(7, 40, 200, 30))
        self.translationXInput.setObjectName("translationXInput")
        self.translationXInput.setFont(font)
        self.translationXInput.setText("(x0,y0,z0),(x1,y1,z1),...")
        self.translationXInput.adjustSize()
        
        self.translationXInput2 = QtWidgets.QLabel(self.centralwidget)
        self.translationXInput2.setGeometry(QtCore.QRect(7, 15, 200, 30))
        self.translationXInput2.setObjectName("translationXInput2")
        self.translationXInput2.setFont(font)
        self.translationXInput2.setText("(x0,y0,z0),(x1,y1,z1),...")
        self.translationXInput2.adjustSize()