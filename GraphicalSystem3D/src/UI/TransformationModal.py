from PyQt5 import QtCore, QtGui, QtWidgets

import numpy as np

from utils.matrixOperations import matrixComposition, createTransformationMatrix

from structures.Wireframe import Wireframe


class TransformationModal(object):
    def setupUi(
        self, MainWindow, currentObject: str, updateObject, closeModal, addToLog
    ):
        self.currentObject = currentObject
        self.updateObject = updateObject
        self.closeModal = closeModal
        self.addToLog = addToLog
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(330, 500)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(12)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.objectName = QtWidgets.QLabel(self.centralwidget)
        self.objectName.setGeometry(QtCore.QRect(7, 18, 320, 30))
        self.objectName.setObjectName("objectName")
        self.objectName.setText(self.currentObject.getName())
        self.objectName.setFont(font)
        self.objectName.adjustSize()
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(9, 59, 311, 340))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        font.setPointSize(10)
        self.translationCheckbox = QtWidgets.QCheckBox(self.frame)
        self.translationCheckbox.setGeometry(QtCore.QRect(10, 60, 91, 31))
        self.translationCheckbox.setObjectName("translationCheckbox")
        self.translationCheckbox.clicked.connect(
            lambda: self.addToOperations("TRANSLATION")
        )
        self.translationCheckbox.setFont(font)
        self.scalingCheckbox = QtWidgets.QCheckBox(self.frame)
        self.scalingCheckbox.setGeometry(QtCore.QRect(10, 140, 91, 31))
        self.scalingCheckbox.setObjectName("scalingCheckbox")
        self.scalingCheckbox.clicked.connect(lambda: self.addToOperations("SCALING"))
        self.scalingCheckbox.setFont(font)
        self.rotationCheckbox = QtWidgets.QCheckBox(self.frame)
        self.rotationCheckbox.setGeometry(QtCore.QRect(10, 220, 91, 31))
        self.rotationCheckbox.setObjectName("rotationCheckbox")
        self.rotationCheckbox.clicked.connect(lambda: self.addToOperations("ROTATION"))
        self.rotationCheckbox.setFont(font)


        self.fillingButton = QtWidgets.QPushButton(self.frame)
        self.fillingButton.setGeometry(QtCore.QRect(10, 0, 85, 23))
        self.fillingButton.setFont(font)
        self.fillingButton.setText("FILL")
        self.fillingButton.clicked.connect(
            (lambda: self.fill())
        )
        self.fillingButton.adjustSize()

        self.translationXInput = QtWidgets.QLineEdit(self.frame)
        self.translationXInput.setGeometry(QtCore.QRect(130, 80, 71, 21))
        self.translationXInput.setObjectName("translationXInput")
        self.translationXInput.setFont(font)
        self.translationYInput = QtWidgets.QLineEdit(self.frame)
        self.translationYInput.setGeometry(QtCore.QRect(230, 80, 71, 20))
        self.translationYInput.setObjectName("translationYInput")
        self.translationYInput.setFont(font)
        self.translationXLabel = QtWidgets.QLabel(self.frame)
        self.translationXLabel.setGeometry(QtCore.QRect(130, 50, 71, 16))
        self.translationXLabel.setObjectName("translationXLabel")
        self.translationXLabel.setFont(font)
        self.translationYLabel = QtWidgets.QLabel(self.frame)
        self.translationYLabel.setGeometry(QtCore.QRect(230, 50, 71, 16))
        self.translationYLabel.setObjectName("translationYLabel")
        self.translationYLabel.setFont(font)

        self.scalingXInput = QtWidgets.QLineEdit(self.frame)
        self.scalingXInput.setGeometry(QtCore.QRect(130, 160, 71, 20))
        self.scalingXInput.setObjectName("scalingXInput")
        self.scalingXInput.setFont(font)
        self.scalingYInput = QtWidgets.QLineEdit(self.frame)
        self.scalingYInput.setGeometry(QtCore.QRect(230, 160, 71, 20))
        self.scalingYInput.setObjectName("scalingYInput")
        self.scalingYInput.setFont(font)
        self.scalingXLabel = QtWidgets.QLabel(self.frame)
        self.scalingXLabel.setGeometry(QtCore.QRect(130, 130, 71, 16))
        self.scalingXLabel.setObjectName("scalingXLabel")
        self.scalingXLabel.setFont(font)
        self.scalingYLabel = QtWidgets.QLabel(self.frame)
        self.scalingYLabel.setGeometry(QtCore.QRect(230, 130, 71, 16))
        self.scalingYLabel.setObjectName("scalingYLabel")
        self.scalingYLabel.setFont(font)

        font.setPointSize(11)
        self.confirmTransformButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmTransformButton.setGeometry(QtCore.QRect(40, 430, 85, 23))
        self.confirmTransformButton.setObjectName("confirmTransformButton")
        self.confirmTransformButton.clicked.connect(lambda: self.confirmHandler())
        self.confirmTransformButton.setFont(font)

        self.resetTransformButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetTransformButton.setGeometry(QtCore.QRect(200, 430, 85, 23))
        self.resetTransformButton.setObjectName("resetTransformButton")
        self.resetTransformButton.clicked.connect(lambda: self.resetHandler())
        self.resetTransformButton.setFont(font)

        font.setPointSize(10)
        self.rotationInput = QtWidgets.QLineEdit(self.frame)
        self.rotationInput.setGeometry(QtCore.QRect(130, 235, 171, 20))
        self.rotationInput.setObjectName("rotationInput")
        self.rotationInput.setFont(font)
        self.rotationLabel = QtWidgets.QLabel(self.frame)
        self.rotationLabel.setGeometry(QtCore.QRect(130, 215, 71, 16))
        self.rotationLabel.setObjectName("rotationLabel")
        self.rotationLabel.setFont(font)

        self.rotationTypeSelf = QtWidgets.QRadioButton(self.frame)
        self.rotationTypeSelf.setGeometry(QtCore.QRect(15, 265, 60, 20))
        self.rotationTypeSelf.setFont(font)
        self.rotationTypeSelf.setObjectName("rotationTypeSelf")
        self.rotationTypeSelf.clicked.connect(lambda: self.setTypeOfRotation("SELF"))
        self.rotationTypeSelf.setChecked(True)
        self.rotationType = "SELF"

        self.rotationTypeOrigin = QtWidgets.QRadioButton(self.frame)
        self.rotationTypeOrigin.setGeometry(QtCore.QRect(15, 290, 70, 20))
        self.rotationTypeOrigin.setObjectName("rotationTypeOrigin")
        self.rotationTypeOrigin.clicked.connect(
            lambda: self.setTypeOfRotation("ORIGIN")
        )
        self.rotationTypeOrigin.setFont(font)

        self.rotationTypePoint = QtWidgets.QRadioButton(self.frame)
        self.rotationTypePoint.setGeometry(QtCore.QRect(15, 315, 50, 22))
        self.rotationTypePoint.setObjectName("rotationTypePoint")
        self.rotationTypePoint.clicked.connect(lambda: self.setTypeOfRotation("POINT"))
        self.rotationTypePoint.setFont(font)

        self.rotatioTypePointXInput = QtWidgets.QLineEdit(self.frame)
        self.rotatioTypePointXInput.setGeometry(QtCore.QRect(130, 315, 71, 20))
        self.rotatioTypePointXInput.setObjectName("rotatioTypePointXInput")
        self.rotatioTypePointXInput.setFont(font)
        self.rotatioTypePointYInput = QtWidgets.QLineEdit(self.frame)
        self.rotatioTypePointYInput.setGeometry(QtCore.QRect(230, 315, 71, 20))
        self.rotatioTypePointYInput.setObjectName("rotatioTypePointYInput")
        self.rotatioTypePointYInput.setFont(font)
        self.rotatioTypePointXLabel = QtWidgets.QLabel(self.frame)
        self.rotatioTypePointXLabel.setGeometry(QtCore.QRect(130, 290, 71, 16))
        self.rotatioTypePointXLabel.setObjectName("rotatioTypePointXLabel")
        self.rotatioTypePointXLabel.setFont(font)
        self.rotatioTypePointYLabel = QtWidgets.QLabel(self.frame)
        self.rotatioTypePointYLabel.setGeometry(QtCore.QRect(230, 290, 71, 16))
        self.rotatioTypePointYLabel.setObjectName("rotatioTypePointYLabel")
        self.rotatioTypePointYLabel.setFont(font)

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
        self.rotationTypeSelf.setText("Self")
        self.rotationTypeOrigin.setText("Origin")
        self.rotationTypePoint.setText("Point: ")
        self.rotationTypePoint.adjustSize()
        self.rotatioTypePointXLabel.setText("Point X")
        self.rotatioTypePointYLabel.setText("Point Y")

    def confirmHandler(self):
        if not len(self.operations_order):
            self.addToLog("Select at least one transformation.")
            return

        if all(
            [
                self.verifyValidTransformationInputs(matrix)
                for matrix in self.operations_order
            ]
        ):
            matrix = self.createMatrix(self.operations_order.pop(0))
            for operation in self.operations_order:
                new_matrix = self.createMatrix(operation)
                matrix = matrixComposition([matrix, new_matrix])

            self.currentObject.applyTransformations(matrix)
            self.updateObject()
            self.closeModal()
        else:
            self.addToLog("Make sure all inputs are defined.")

    def resetHandler(self):
        self.currentObject.reset()
        self.updateObject()
        self.closeModal()

    def verifyValidTransformationInputs(self, operation: str) -> bool:
        if operation == "TRANSLATION":
            if (
                self.translationXInput.text() == ""
                or self.translationYInput.text() == ""
            ):
                return False
        elif operation == "SCALING":
            if self.scalingXInput.text() == "" or self.scalingYInput.text() == "":
                return False
        elif operation == "ROTATION":
            if self.rotationInput.text() == "":
                return False
            elif self.rotationType == "POINT":
                if (
                    self.rotatioTypePointXInput.text() == ""
                    or self.rotatioTypePointYInput.text() == ""
                ):
                    return False
        return True

    def createMatrix(self, operation: str) -> np.matrix:
        if operation == "TRANSLATION":
            data = {
                "xInput": float(self.translationXInput.text()),
                "yInput": float(self.translationYInput.text()),
            }

            return createTransformationMatrix(operation=operation, data=data)

        if operation == "SCALING":
            center = self.currentObject.calculateGeometricCenter()

            data = {
                "centerX": center[0],
                "centerY": center[1],
                "xInput": self.scalingXInput.text(),
                "yInput": self.scalingYInput.text(),
            }

            return createTransformationMatrix(operation=operation, data=data)

        if operation == "ROTATION":
            data = {"rotation": self.rotationInput.text(), "type": self.rotationType}

            if self.rotationType == "SELF":
                center = self.currentObject.calculateGeometricCenter()
                data["centerX"] = center[0]
                data["centerY"] = center[1]
            elif self.rotationType == "POINT":
                data["pointX"] = float(self.rotatioTypePointXInput.text())
                data["pointY"] = float(self.rotatioTypePointYInput.text())

            return createTransformationMatrix("ROTATION", data)

    def fill(self):
        if isinstance(self.currentObject, Wireframe):
            self.currentObject.fill()
            self.updateObject()

    def addToOperations(self, operation: str):
        if operation in self.operations_order:
            self.operations_order.remove(operation)
        else:
            self.operations_order.append(operation)

    def setTypeOfRotation(self, type: str) -> None:
        self.rotationType = type
