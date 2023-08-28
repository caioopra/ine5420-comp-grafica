from PyQt5 import QtCore, QtGui, QtWidgets

import numpy as np
from utils.matrixOperations import generateMatrix, matrixComposition

from DisplayFile import displayFile


class TransformationModal(object):
    def setupUi(self, MainWindow, objectName: str):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(330, 460)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.objectName = QtWidgets.QLabel(self.centralwidget)
        self.objectName.setGeometry(QtCore.QRect(6, 18, 320, 30))
        self.objectName.setObjectName("objectName")
        self.objectName.setText(objectName)
        self.objectName.adjustSize()
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(9, 59, 311, 241))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.translationCheckbox = QtWidgets.QCheckBox(self.frame)
        self.translationCheckbox.setGeometry(QtCore.QRect(10, 20, 91, 31))
        self.translationCheckbox.setObjectName("translationCheckbox")
        self.translationCheckbox.clicked.connect(
            lambda: self.addToOperations("TRANSLATION")
        )
        self.scalingCheckbox = QtWidgets.QCheckBox(self.frame)
        self.scalingCheckbox.setGeometry(QtCore.QRect(10, 100, 91, 31))
        self.scalingCheckbox.setObjectName("scalingCheckbox")
        self.scalingCheckbox.clicked.connect(lambda: self.addToOperations("SCALING"))
        self.rotationCheckbox = QtWidgets.QCheckBox(self.frame)
        self.rotationCheckbox.setGeometry(QtCore.QRect(10, 180, 91, 31))
        self.rotationCheckbox.setObjectName("rotationCheckbox")
        self.rotationCheckbox.clicked.connect(lambda: self.addToOperations("ROTATION"))

        self.translationXInput = QtWidgets.QLineEdit(self.frame)
        self.translationXInput.setGeometry(QtCore.QRect(130, 40, 71, 21))
        self.translationXInput.setObjectName("translationXInput")
        self.translationYInput = QtWidgets.QLineEdit(self.frame)
        self.translationYInput.setGeometry(QtCore.QRect(230, 40, 71, 20))
        self.translationYInput.setObjectName("translationYInput")
        self.translationXLabel = QtWidgets.QLabel(self.frame)
        self.translationXLabel.setGeometry(QtCore.QRect(130, 10, 71, 16))
        self.translationXLabel.setObjectName("translationXLabel")
        self.translationYLabel = QtWidgets.QLabel(self.frame)
        self.translationYLabel.setGeometry(QtCore.QRect(230, 10, 71, 16))
        self.translationYLabel.setObjectName("translationYLabel")

        self.rotationInput = QtWidgets.QLineEdit(self.frame)
        self.rotationInput.setGeometry(QtCore.QRect(130, 195, 171, 20))
        self.rotationInput.setObjectName("rotationInput")
        self.rotationLabel = QtWidgets.QLabel(self.frame)
        self.rotationLabel.setGeometry(QtCore.QRect(130, 175, 71, 16))
        self.rotationLabel.setObjectName("rotationLabel")

        self.scalingXInput = QtWidgets.QLineEdit(self.frame)
        self.scalingXInput.setGeometry(QtCore.QRect(130, 120, 71, 20))
        self.scalingXInput.setObjectName("scalingXInput")
        self.scalingYInput = QtWidgets.QLineEdit(self.frame)
        self.scalingYInput.setGeometry(QtCore.QRect(230, 120, 71, 20))
        self.scalingYInput.setObjectName("scalingYInput")
        self.scalingXLabel = QtWidgets.QLabel(self.frame)
        self.scalingXLabel.setGeometry(QtCore.QRect(230, 90, 71, 16))
        self.scalingXLabel.setObjectName("scalingXLabel")
        self.scalingYLabel = QtWidgets.QLabel(self.frame)
        self.scalingYLabel.setGeometry(QtCore.QRect(130, 90, 71, 16))
        self.scalingYLabel.setObjectName("scalingYLabel")

        self.confirmTransformButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmTransformButton.setGeometry(QtCore.QRect(40, 330, 85, 23))
        self.confirmTransformButton.setObjectName("confirmTransformButton")
        self.confirmTransformButton.clicked.connect(lambda: self.confirmHandler())
        self.resetTransformButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetTransformButton.setGeometry(QtCore.QRect(200, 330, 85, 23))
        self.resetTransformButton.setObjectName("resetTransformButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 330, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.operations_order = []

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainwWindow"))
        self.translationCheckbox.setText(_translate("MainWindow", "Translation"))
        self.translationCheckbox.adjustSize()
        self.scalingCheckbox.setText(_translate("MainWindow", "Scaling"))
        self.rotationCheckbox.setText(_translate("MainWindow", "Rotation"))
        self.translationXLabel.setText(_translate("MainWindow", "X"))
        self.translationYLabel.setText(_translate("MainWindow", "Y"))
        self.rotationLabel.setText(_translate("MainWindow", "Rotation (degrees)"))
        self.rotationLabel.adjustSize()
        self.scalingXLabel.setText(_translate("MainWindow", "X"))
        self.scalingYLabel.setText(_translate("MainWindow", "Y"))
        self.confirmTransformButton.setText("Confirm")
        self.resetTransformButton.setText("Reset")

    def confirmHandler(self):
        if not len(self.operations_order):
            print("selecione uma operação")  # TODO: add to log
            return

        matrix = self.createMatrix(self.operations_order.pop(0))
        for operation in self.operations_order:
            new_matrix = self.createMatrix(operation)
            matrix = matrixComposition(matrix, new_matrix)

        print(matrix)

    def createMatrix(self, operation: str) -> np.matrix:
        if operation == "TRANSLATION":
            return generateMatrix(
                operation,
                float(self.translationXInput.text()),
                float(self.translationYInput.text()),
            )

        if operation == "SCALING":
            return generateMatrix(
                operation,
                float(self.scalingXInput.text()),
                float(self.scalingYInput.text()),
            )

        if operation == "ROTATION":
            return generateMatrix(
                operation,
                float(self.rotationInput.text()),
            )

    def addToOperations(self, operation: str):
        if operation in self.operations_order:
            self.operations_order.remove(operation)
        else:
            self.operations_order.append(operation)
