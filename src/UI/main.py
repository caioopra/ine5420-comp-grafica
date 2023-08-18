# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1097, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.viewport = QtWidgets.QLabel(self.centralwidget)
        self.viewport.setGeometry(QtCore.QRect(336, 6, 761, 491))
        self.viewport.setAutoFillBackground(False)
        self.viewport.setObjectName("viewport")

        self.objectsList = QtWidgets.QListWidget(self.centralwidget)
        self.objectsList.setGeometry(QtCore.QRect(10, 10, 311, 221))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(10)
        self.objectsList.setFont(font)
        self.objectsList.setObjectName("objectsList")

        self.logField = QtWidgets.QListWidget(self.centralwidget)
        self.logField.setGeometry(QtCore.QRect(336, 500, 761, 151))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(10)
        self.logField.setFont(font)
        self.logField.setObjectName("logField")

        self.menuFrame = QtWidgets.QFrame(self.centralwidget)
        self.menuFrame.setGeometry(QtCore.QRect(5, 0, 330, 681))
        self.menuFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menuFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menuFrame.setObjectName("menuFrame")

        # naviagation buttons
        self.navigateUpButton = QtWidgets.QToolButton(self.menuFrame)
        self.navigateUpButton.setGeometry(QtCore.QRect(140, 350, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        self.navigateUpButton.setFont(font)
        self.navigateUpButton.setAutoRaise(True)
        self.navigateUpButton.setArrowType(QtCore.Qt.UpArrow)
        self.navigateUpButton.setObjectName("navigateUpButton")
        self.navigateRightButton = QtWidgets.QToolButton(self.menuFrame)
        self.navigateRightButton.setGeometry(QtCore.QRect(180, 390, 40, 40))
        self.navigateRightButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.navigateRightButton.setToolTipDuration(0)
        self.navigateRightButton.setAutoRaise(True)
        self.navigateRightButton.setArrowType(QtCore.Qt.RightArrow)
        self.navigateRightButton.setObjectName("navigateRightButton")
        self.navigateLeftButton = QtWidgets.QToolButton(self.menuFrame)
        self.navigateLeftButton.setGeometry(QtCore.QRect(100, 390, 40, 40))
        self.navigateLeftButton.setAutoRaise(True)
        self.navigateLeftButton.setArrowType(QtCore.Qt.LeftArrow)
        self.navigateLeftButton.setObjectName("navigateLeftButton")
        self.navigateDownButton = QtWidgets.QToolButton(self.menuFrame)
        self.navigateDownButton.setGeometry(QtCore.QRect(140, 430, 40, 40))
        self.navigateDownButton.setAutoRaise(True)
        self.navigateDownButton.setArrowType(QtCore.Qt.DownArrow)
        self.navigateDownButton.setObjectName("navigateDownButton")

        # zoom buttons
        self.zoomOutButton = QtWidgets.QPushButton(self.menuFrame)
        self.zoomOutButton.setGeometry(QtCore.QRect(20, 350, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(10)
        self.zoomOutButton.setFont(font)
        self.zoomOutButton.setObjectName("zoomOutButton")
        self.zoomInButton = QtWidgets.QPushButton(self.menuFrame)
        self.zoomInButton.setGeometry(QtCore.QRect(230, 350, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(10)
        self.zoomInButton.setFont(font)
        self.zoomInButton.setObjectName("zoomInButton")

        self.deleteButton = QtWidgets.QPushButton(self.menuFrame)
        self.deleteButton.setGeometry(QtCore.QRect(115, 290, 90, 32))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(11)
        self.deleteButton.setFont(font)
        self.deleteButton.setObjectName("deleteButton")
        self.confirmButton = QtWidgets.QPushButton(self.menuFrame)
        self.confirmButton.setGeometry(QtCore.QRect(225, 290, 90, 32))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(11)
        self.confirmButton.setFont(font)
        self.confirmButton.setObjectName("confirmButton")
        self.cancelButton = QtWidgets.QPushButton(self.menuFrame)
        self.cancelButton.setGeometry(QtCore.QRect(10, 290, 90, 32))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(11)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")

        # radio buttons
        self.lineRadioButton = QtWidgets.QRadioButton(self.menuFrame)
        self.lineRadioButton.setGeometry(QtCore.QRect(130, 240, 90, 32))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(11)
        self.lineRadioButton.setFont(font)
        self.lineRadioButton.setObjectName("lineRadioButton")

        self.polygonRadioButton = QtWidgets.QRadioButton(self.menuFrame)
        self.polygonRadioButton.setGeometry(QtCore.QRect(230, 240, 90, 32))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(11)
        self.polygonRadioButton.setFont(font)
        self.polygonRadioButton.setObjectName("polygonRadioButton")

        self.pointRadioButton = QtWidgets.QRadioButton(self.menuFrame)
        self.pointRadioButton.setGeometry(QtCore.QRect(10, 240, 90, 32))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(11)
        self.pointRadioButton.setFont(font)
        self.pointRadioButton.setObjectName("pointRadioButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1097, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.viewport.setText(_translate("MainWindow", "VIEWPORT"))
        self.navigateUpButton.setText(_translate("MainWindow", "..."))
        self.navigateRightButton.setText(_translate("MainWindow", "..."))
        self.navigateLeftButton.setText(_translate("MainWindow", "..."))
        self.navigateDownButton.setText(_translate("MainWindow", "..."))
        self.zoomOutButton.setText(_translate("MainWindow", "Zoom out"))
        self.zoomInButton.setText(_translate("MainWindow", "Zoom in"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.confirmButton.setText(_translate("MainWindow", "Confirm"))
        self.cancelButton.setText(_translate("MainWindow", "Cancel"))
        self.lineRadioButton.setText(_translate("MainWindow", "Line"))
        self.polygonRadioButton.setText(_translate("MainWindow", "Polygon"))
        self.pointRadioButton.setText(_translate("MainWindow", "Point"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
