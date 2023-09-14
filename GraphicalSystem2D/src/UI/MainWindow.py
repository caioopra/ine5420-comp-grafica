from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QColorDialog

from UI.Viewport import Viewport
from UI.TransformationModal import TransformationModal
from UI.OpenFileModal import OpenFileModal

from DisplayFile import displayFile
from utils.writeObjFile import writeObjectsToFile

from structures.Point import Point

from utils.matrixOperations import generateMatrix, matrixComposition


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.pressed_position = None
        self.__currentColor = QtCore.Qt.red
        self.clicked = QtCore.pyqtSignal()
        MainWindow.setMouseTracking(True)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.viewport = Viewport(MainWindow)
        self.viewport.setGeometry(
            QtCore.QRect(
                335,
                5,
                760,
                490,
            )
        )
        self.viewport.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.viewport.setStyleSheet("background-color: #fff")
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

        self.mainWindow = MainWindow

        self.objectsList = QtWidgets.QListWidget(self.menuFrame)
        self.objectsList.setGeometry(QtCore.QRect(10, 10, 311, 221))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(10)
        self.objectsList.setFont(font)
        self.objectsList.setObjectName("objectsList")
        self.objectsList.doubleClicked.connect(
            lambda: self.openTransformationModal(self.objectsList.currentItem().text())
        )

        # navigation buttons
        self.navigateUpButton = QtWidgets.QToolButton(self.menuFrame)
        self.navigateUpButton.setGeometry(QtCore.QRect(140, 350, 40, 40))
        self.navigateUpButton.setFont(font)
        self.navigateUpButton.setAutoRaise(True)
        self.navigateUpButton.setArrowType(QtCore.Qt.UpArrow)
        self.navigateUpButton.setObjectName("navigateUpButton")
        self.navigateUpButton.clicked.connect(lambda: self.navigate("UP"))

        self.navigateRightButton = QtWidgets.QToolButton(self.menuFrame)
        self.navigateRightButton.setGeometry(QtCore.QRect(180, 390, 40, 40))
        self.navigateRightButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.navigateRightButton.setToolTipDuration(0)
        self.navigateRightButton.setAutoRaise(True)
        self.navigateRightButton.setArrowType(QtCore.Qt.RightArrow)
        self.navigateRightButton.setObjectName("navigateRightButton")
        self.navigateRightButton.clicked.connect(lambda: self.navigate("RIGHT"))

        self.navigateLeftButton = QtWidgets.QToolButton(self.menuFrame)
        self.navigateLeftButton.setGeometry(QtCore.QRect(100, 390, 40, 40))
        self.navigateLeftButton.setAutoRaise(True)
        self.navigateLeftButton.setArrowType(QtCore.Qt.LeftArrow)
        self.navigateLeftButton.setObjectName("navigateLeftButton")
        self.navigateLeftButton.clicked.connect(lambda: self.navigate("LEFT"))

        self.navigateDownButton = QtWidgets.QToolButton(self.menuFrame)
        self.navigateDownButton.setGeometry(QtCore.QRect(140, 430, 40, 40))
        self.navigateDownButton.setAutoRaise(True)
        self.navigateDownButton.setArrowType(QtCore.Qt.DownArrow)
        self.navigateDownButton.setObjectName("navigateDownButton")
        self.navigateDownButton.clicked.connect(lambda: self.navigate("DOWN"))

        font.setPointSize(11)
        self.objectNameInputLabel = QtWidgets.QLabel(self.menuFrame)
        self.objectNameInputLabel.setGeometry(QtCore.QRect(10, 500, 300, 30))
        self.objectNameInputLabel.setFont(font)
        self.objectNameInputLabel.setText("Object name:")
        self.objectNameInput = QtWidgets.QLineEdit(self.menuFrame)
        self.objectNameInput.setGeometry(QtCore.QRect(10, 525, 300, 32))
        self.objectNameInput.setFont(font)

        # zoom buttons
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(10)
        self.zoomOutButton = QtWidgets.QPushButton(self.menuFrame)
        self.zoomOutButton.setGeometry(QtCore.QRect(20, 350, 75, 23))
        self.zoomOutButton.setFont(font)
        self.zoomOutButton.setObjectName("zoomOutButton")
        self.zoomOutButton.clicked.connect(lambda: self.zoom("OUT"))

        self.zoomInButton = QtWidgets.QPushButton(self.menuFrame)
        self.zoomInButton.setGeometry(QtCore.QRect(230, 350, 75, 23))
        self.zoomInButton.setFont(font)
        self.zoomInButton.setObjectName("zoomInButton")
        self.zoomInButton.clicked.connect(lambda: self.zoom("IN"))

        # selection buttons
        self.deleteButton = QtWidgets.QPushButton(self.menuFrame)
        self.deleteButton.setGeometry(QtCore.QRect(115, 290, 90, 32))
        font.setPointSize(11)
        self.deleteButton.setFont(font)
        self.deleteButton.setObjectName("deleteButton")
        self.deleteButton.clicked.connect(lambda: self.handleDeleteClick())

        self.confirmButton = QtWidgets.QPushButton(self.menuFrame)
        self.confirmButton.setGeometry(QtCore.QRect(225, 290, 90, 32))
        self.confirmButton.setFont(font)
        self.confirmButton.setObjectName("confirmButton")
        self.confirmButton.clicked.connect(
            lambda: self.handleConfirmClick(self.objectNameInput.text())
        )
        self.cancelButton = QtWidgets.QPushButton(self.menuFrame)
        self.cancelButton.setGeometry(QtCore.QRect(10, 290, 90, 32))
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        self.cancelButton.clicked.connect(lambda: self.handleCancelClick())

        self.selectColorButton = QtWidgets.QPushButton(self.menuFrame)
        self.selectColorButton.setGeometry(QtCore.QRect(213, 395, 108, 40))
        self.selectColorButton.setFont(font)
        self.selectColorButton.setObjectName("selectButton")
        self.selectColorButton.clicked.connect(lambda: self.handleColorSelectionClick())

        # radio buttons
        self.lineRadioButton = QtWidgets.QRadioButton(self.menuFrame)
        self.lineRadioButton.clicked.connect(lambda: self.setObjectTypeSelected("LINE"))
        self.lineRadioButton.setGeometry(QtCore.QRect(125, 240, 90, 32))
        self.lineRadioButton.setFont(font)
        self.lineRadioButton.setObjectName("lineRadioButton")

        self.wireframeRadioButton = QtWidgets.QRadioButton(self.menuFrame)
        self.wireframeRadioButton.clicked.connect(
            lambda: self.setObjectTypeSelected("WIREFRAME")
        )
        self.wireframeRadioButton.setGeometry(QtCore.QRect(225, 245, 90, 30))
        self.wireframeRadioButton.setFont(font)
        self.wireframeRadioButton.setObjectName("wireframeRadioButton")

        self.pointRadioButton = QtWidgets.QRadioButton(self.menuFrame)
        self.pointRadioButton.clicked.connect(
            lambda: self.setObjectTypeSelected("POINT")
        )
        self.pointRadioButton.setGeometry(QtCore.QRect(10, 240, 90, 32))
        self.pointRadioButton.setFont(font)
        self.pointRadioButton.setObjectName("pointRadioButton")

        font.setPointSize(10)
        self.rotationAmountLabel = QtWidgets.QLabel(self.menuFrame)
        self.rotationAmountLabel.setGeometry(QtCore.QRect(17, 375, 130, 30))
        self.rotationAmountLabel.setFont(font)
        self.rotationAmountLabel.setText("Rot./zoom %")
        self.rotationAmountInput = QtWidgets.QLineEdit(self.menuFrame)
        self.rotationAmountInput.setGeometry(QtCore.QRect(30, 397, 50, 30))
        self.rotationAmountInput.setFont(font)
        self.rotationAmountInput.setObjectName("rotationAmountInput")
        self.rotationAmountInput.setText("10")
        self.rotationAmountInput.textChanged.connect(self.changeZoomRotAmount)

        self.rotateWindowRight = QtWidgets.QPushButton(self.menuFrame)
        self.rotateWindowRight.setGeometry(QtCore.QRect(250, 430, 45, 45))
        self.rotateWindowRight.setObjectName("rotateWindowRight")
        self.rotateWindowRight.setIcon(QtGui.QIcon("UI/img/rotate_right.png"))
        self.rotateWindowRight.clicked.connect(lambda: self.rotateWindow("RIGHT", self.rotationAmountInput.text()))

        self.rotateWindowLeft = QtWidgets.QPushButton(self.menuFrame)
        self.rotateWindowLeft.setGeometry(QtCore.QRect(32, 430, 45, 45))
        self.rotateWindowLeft.setObjectName("rotateWindowLeft")
        self.rotateWindowLeft.setIcon(QtGui.QIcon("UI/img/rotate_left.png"))
        self.rotateWindowLeft.clicked.connect(lambda: self.rotateWindow("LEFT", self.rotationAmountInput.text()))

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
        self.wireframeRadioButton.setText(_translate("MainWindow", "Wireframe"))
        self.wireframeRadioButton.adjustSize()
        self.pointRadioButton.setText(_translate("MainWindow", "Point"))
        self.selectColorButton.setText(_translate("MainWindow", "Select Color"))
        self.selectColorButton.adjustSize()

    def setObjectTypeSelected(self, event):
        displayFile.clearBuffer()
        self.viewport.update()
        self.viewport.currentSelectedType = event

    def handleConfirmClick(self, name: str) -> None:
        if name == "":
            self.openFileModal()
            return

        dict = displayFile.tryRegistering(
            self.viewport.currentSelectedType, name, self.__currentColor
        )
        self.logField.addItem(dict["mensagem"])
        if dict["status"] == True:
            self.objectsList.addItem(name)
            self.objectNameInput.clear()

    def handleCancelClick(self) -> None:
        displayFile.clearBuffer()
        self.objectNameInput.clear()
        self.logField.addItem("Cleared.")
        self.viewport.update()

    def handleDeleteClick(self) -> None:
        name = self.objectsList.currentRow()
        name = self.objectsList.takeItem(name)
        if name is not None:
            displayFile.deleteObject(name.text())
            self.viewport.update()
        else:
            self.logField.addItem("[ERROR] No object selected.")

    def handleColorSelectionClick(self) -> None:
        self.openColorDialog()

    def openColorDialog(self) -> None:
        self.__currentColor = QColorDialog.getColor()
        if self.__currentColor.isValid():
            self.viewport.setCurrentColor(self.__currentColor)

    def openTransformationModal(self, objectName: str):
        self.window = QtWidgets.QMainWindow()
        self.ui = TransformationModal()
        self.ui.setupUi(
            self.window,
            currentObject=displayFile.getObjectByName(objectName),
            updateObject=self.viewport.update,
            closeModal=self.window.close,
            addToLog=self.logField.addItem,
        )
        self.window.show()

    def navigate(self, direction: str):
        displayFile.navigate(direction)
        self.viewport.update()

    def changeZoomRotAmount(self) -> None:
        displayFile.getWindow().setRotationZoomPercentage(
            self.rotationAmountInput.text()
        )

    def zoom(self, direction: str):
        displayFile.zoom(direction)
        self.viewport.update()

    def rotateWindow(self, direction: str, amount: str):
        x, y = displayFile.getCenter()
        for point in displayFile.getPoints():
            matrix = generateMatrix(
                "TRANSLATION",
                float(-x),
                float(-y),
            )
            point.applyTransformations(matrix)
            rotation_matrix = generateMatrix("ROTATION", amount)
            point.applyTransformations(rotation_matrix)

        for line in displayFile.getLines():
            if line.getName() != None:
                matrix = generateMatrix(
                    "TRANSLATION",
                    float(-x),
                    float(-y),
                )
                line.applyTransformations(matrix)
                rotation_matrix = generateMatrix("ROTATION", amount)
                line.applyTransformations(rotation_matrix)

        for wireframe in displayFile.getWireframes():
            matrix = generateMatrix(
                "TRANSLATION",
                float(-x),
                float(-y),
            )
            wireframe.applyTransformations(matrix)
            rotation_matrix = generateMatrix("ROTATION", amount)
            wireframe.applyTransformations(rotation_matrix)
        displayFile.move_to_center()
        self.viewport.update()
        '''
        if direction == "LEFT":
            ...
        elif direction == "RIGHT":
            ...'''

    def openFileModal(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = OpenFileModal()
        self.ui.setupUi(
            self.window,
            closeModal=self.window.close,
            setWindowDimensions=self.setWindowDimensions,
            getObjectsFromFile=self.getObjectsFromFIle,
            saveObjectsToFile=self.saveObjectsToFile
        )
        self.window.show()

    def setWindowDimensions(self, min, max):
        displayFile.setWindowSize(min, max)

    def getObjectsFromFIle(self, objectsList: list):
        for obj in objectsList:
            obj.setWindow(displayFile.getWindow())
            
            self.objectsList.addItem(obj.getName())
            displayFile.addObjectFromFile(obj)
            
    def saveObjectsToFile(self, filename: str) -> None:
        objects = []
        
        for point in displayFile.getPoints():
            objects.append(point)
        for line in displayFile.getLines():
            objects.append(line)
        for wireframe in displayFile.getWireframes():
            objects.append(wireframe)
            
        window = displayFile.getWindow()
        w_min = Point(window.xw_min, window.yw_min)
        w_max = Point(window.xw_max, window.yw_max)
        
        writeObjectsToFile(filename=filename, objects=objects, window=[w_min, w_max])
        self.window.close()
        
        
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
