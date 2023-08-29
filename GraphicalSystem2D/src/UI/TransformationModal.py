from PyQt5 import QtCore, QtGui, QtWidgets

import numpy as np

from utils.matrixOperations import generateMatrix, matrixComposition


class TransformationModal(object):
    def setupUi(
        self, MainWindow, currentObject: str, updateObject, closeModal, addToLog
    ):
        self.currentObject = currentObject
        self.updateObject = updateObject
        self.closeModal = closeModal
        self.addToLog = addToLog
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(330, 460)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.objectName = QtWidgets.QLabel(self.centralwidget)
        self.objectName.setGeometry(QtCore.QRect(6, 18, 320, 30))
        self.objectName.setObjectName("objectName")
        self.objectName.setText(self.currentObject.getName())
        self.objectName.adjustSize()
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(9, 59, 311, 300))
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

        self.scalingXInput = QtWidgets.QLineEdit(self.frame)
        self.scalingXInput.setGeometry(QtCore.QRect(130, 120, 71, 20))
        self.scalingXInput.setObjectName("scalingXInput")
        self.scalingYInput = QtWidgets.QLineEdit(self.frame)
        self.scalingYInput.setGeometry(QtCore.QRect(230, 120, 71, 20))
        self.scalingYInput.setObjectName("scalingYInput")
        self.scalingXLabel = QtWidgets.QLabel(self.frame)
        self.scalingXLabel.setGeometry(QtCore.QRect(130, 90, 71, 16))
        self.scalingXLabel.setObjectName("scalingXLabel")
        self.scalingYLabel = QtWidgets.QLabel(self.frame)
        self.scalingYLabel.setGeometry(QtCore.QRect(230, 90, 71, 16))
        self.scalingYLabel.setObjectName("scalingYLabel")

        self.confirmTransformButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmTransformButton.setGeometry(QtCore.QRect(40, 380, 85, 23))
        self.confirmTransformButton.setObjectName("confirmTransformButton")
        self.confirmTransformButton.clicked.connect(lambda: self.confirmHandler())
        self.resetTransformButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetTransformButton.setGeometry(QtCore.QRect(200, 380, 85, 23))
        self.resetTransformButton.setObjectName("resetTransformButton")

        self.rotationInput = QtWidgets.QLineEdit(self.frame)
        self.rotationInput.setGeometry(QtCore.QRect(130, 195, 171, 20))
        self.rotationInput.setObjectName("rotationInput")
        self.rotationLabel = QtWidgets.QLabel(self.frame)
        self.rotationLabel.setGeometry(QtCore.QRect(130, 175, 71, 16))
        self.rotationLabel.setObjectName("rotationLabel")

        self.rotationTypeSelf = QtWidgets.QRadioButton(self.frame)
        self.rotationTypeSelf.setGeometry(QtCore.QRect(15, 225, 60, 20))
        # self.rotationTypeSelf.setFont()
        self.rotationTypeSelf.setObjectName("rotationTypeSelf")
        self.rotationTypeSelf.clicked.connect(lambda: self.setTypeOfRotation("SELF"))
        self.rotationTypeSelf.setChecked(True)
        self.rotationType = "SELF"

        self.rotationTypeOrigin = QtWidgets.QRadioButton(self.frame)
        self.rotationTypeOrigin.setGeometry(QtCore.QRect(15, 250, 60, 20))
        # self.rotationTypeOrigin.setFont()
        self.rotationTypeOrigin.setObjectName("rotationTypeOrigin")
        self.rotationTypeOrigin.clicked.connect(
            lambda: self.setTypeOfRotation("ORIGIN")
        )

        self.rotationTypePoint = QtWidgets.QRadioButton(self.frame)
        self.rotationTypePoint.setGeometry(QtCore.QRect(15, 275, 50, 22))
        # self.rotationTypePoint.setFont()
        self.rotationTypePoint.setObjectName("rotationTypePoint")
        self.rotationTypePoint.clicked.connect(lambda: self.setTypeOfRotation("POINT"))

        self.rotatioTypePointXInput = QtWidgets.QLineEdit(self.frame)
        self.rotatioTypePointXInput.setGeometry(QtCore.QRect(130, 275, 71, 20))
        self.rotatioTypePointXInput.setObjectName("rotatioTypePointXInput")
        self.rotatioTypePointYInput = QtWidgets.QLineEdit(self.frame)
        self.rotatioTypePointYInput.setGeometry(QtCore.QRect(230, 275, 71, 20))
        self.rotatioTypePointYInput.setObjectName("rotatioTypePointYInput")
        self.rotatioTypePointXLabel = QtWidgets.QLabel(self.frame)
        self.rotatioTypePointXLabel.setGeometry(QtCore.QRect(230, 250, 71, 16))
        self.rotatioTypePointXLabel.setObjectName("rotatioTypePointXLabel")
        self.rotatioTypePointYLabel = QtWidgets.QLabel(self.frame)
        self.rotatioTypePointYLabel.setGeometry(QtCore.QRect(130, 250, 71, 16))
        self.rotatioTypePointYLabel.setObjectName("rotatioTypePointYLabel")

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

        if self.verifyValidTransformationInputs(self.operations_order[0]):
            matrix = self.createMatrix(self.operations_order.pop(0))
            for operation in self.operations_order:
                new_matrix = self.createMatrix(operation)
                matrix = matrixComposition(matrix, new_matrix)

            self.currentObject.applyTransformations(matrix)
            self.updateObject()
            self.closeModal()
        else:
            self.addToLog("Make sure all inputs are defined.")

    def verifyValidTransformationInputs(self, operation: str) -> bool:
        if operation == "TRANSLATION":
            if self.translationXInput.text() == "" or self.translationYInput.text() == "":
                return False
        elif operation == "SCALING":
            if self.scalingXInput.text() == "" or self.scalingYInput.text() == "":
                return False
        elif operation == "ROTATION":
            if self.rotationInput.text() == "":
                return False
            elif self.rotationType == "POINT":
                if self.rotatioTypePointXInput.text() == "" or self.rotatioTypePointYInput.text() == "":
                    return False
        return True

    def createMatrix(self, operation: str) -> np.matrix:
        if operation == "TRANSLATION":
            return generateMatrix(
                operation,
                float(self.translationXInput.text()),
                float(self.translationYInput.text()),
            )

        if operation == "SCALING":
            center = self.currentObject.calculateGeometricCenter()

            translation_matrix = generateMatrix("TRANSLATION", -center[0], -center[1])
            intermediate = matrixComposition(
                translation_matrix,
                generateMatrix(
                    "SCALING", self.scalingXInput.text(), self.scalingYInput.text()
                ),
            )
            return matrixComposition(
                intermediate, generateMatrix("TRANSLATION", center[0], center[1])
            )

        if operation == "ROTATION":
            if self.rotationType == "SELF":
                center = self.currentObject.calculateGeometricCenter()

                translation_matrix = generateMatrix(
                    "TRANSLATION", -center[0], -center[1]
                )
                intermediate = matrixComposition(
                    translation_matrix,
                    generateMatrix("ROTATION", self.rotationInput.text()),
                )
                return matrixComposition(
                    intermediate, generateMatrix("TRANSLATION", center[0], center[1])
                )

            elif self.rotationType == "ORIGIN":
                return generateMatrix("ROTATION", self.rotationInput.text())
            elif self.rotationType == "POINT":
                point_x = float(self.rotatioTypePointXInput.text())
                point_y = float(self.rotatioTypePointYInput.text())

                translation_matrix = generateMatrix("TRANSLATION", -point_x, -point_y)
                intermediate = matrixComposition(
                    translation_matrix,
                    generateMatrix("ROTATION", self.rotationInput.text()),
                )
                return matrixComposition(
                    intermediate, generateMatrix("TRANSLATION", point_x, point_y)
                )

    def addToOperations(self, operation: str):
        if operation in self.operations_order:
            self.operations_order.remove(operation)
        else:
            self.operations_order.append(operation)

    # TODO: set self center as default on the radio button
    def setTypeOfRotation(self, type: str) -> None:
        self.rotationType = type
