from PyQt5 import QtCore, QtGui, QtWidgets
from structures.Point import Point


class Object3DCreationModal(object):
    def setupUi(self, MainWindow, closeModal, createObject):
        self.closeModal = closeModal
        self.createObject = createObject
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 400)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(11)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        # ==========================
        # ======== X INPUT =========
        self.translationXInput = QtWidgets.QLabel(self.centralwidget)
        self.translationXInput.setGeometry(QtCore.QRect(5, 20, 195, 30))
        self.translationXInput.setObjectName("translationXInput")
        self.translationXInput.setFont(font)
        self.translationXInput.setText("Input: (x0,y0,z0),(x1,y1,z1),...")
        self.translationXInput.adjustSize()

        self.pointsInput = QtWidgets.QLineEdit(self.centralwidget)
        self.pointsInput.setGeometry(QtCore.QRect(5, 50, 290, 30))
        self.pointsInput.setObjectName("pointsInput")
        self.pointsInput.setFont(font)
        self.pointsInput.setText("(0,0,0),(100, 100, 100),(200,200,200)")  # TODO> remove this

        self.confirmTransformButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmTransformButton.setGeometry(QtCore.QRect(10, 85, 130, 25))
        self.confirmTransformButton.setObjectName("confirmTransformButton")
        self.confirmTransformButton.setFont(font)
        self.confirmTransformButton.setText("Confirm")
        self.confirmTransformButton.clicked.connect(
            lambda: self._confirmHandler(self.pointsInput.text())
        )

        self.cancelTransformButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelTransformButton.setGeometry(QtCore.QRect(160, 85, 130, 25))
        self.cancelTransformButton.setObjectName("cancelTransformButton")
        self.cancelTransformButton.setFont(font)
        self.cancelTransformButton.setText("Cancel")
        self.cancelTransformButton.clicked.connect(lambda: self.pointsInput.setText(""))

        self.objectNameInputLabel = QtWidgets.QLabel(self.centralwidget)
        self.objectNameInputLabel.setGeometry(QtCore.QRect(5, 150, 80, 30))
        self.objectNameInputLabel.setObjectName("objectNameInputLabel")
        self.objectNameInputLabel.setFont(font)
        self.objectNameInputLabel.setText("Object name:")
        self.objectNameInputLabel.adjustSize()

        self.objectNameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.objectNameInput.setGeometry(QtCore.QRect(120, 148, 165, 25))
        self.objectNameInput.setObjectName("objectNameInput")
        self.objectNameInput.setFont(font)
        
        self.edgesInputLabel = QtWidgets.QLabel(self.centralwidget)
        self.edgesInputLabel.setGeometry(QtCore.QRect(5, 200, 80, 30))
        self.edgesInputLabel.setObjectName("edgesInputLabel")
        self.edgesInputLabel.setFont(font)
        self.edgesInputLabel.setText("Edges <(0,1),(1,3),...>:")
        self.edgesInputLabel.adjustSize()

        self.edgesInput = QtWidgets.QLineEdit(self.centralwidget)
        self.edgesInput.setGeometry(QtCore.QRect(5, 240, 165, 25))
        self.edgesInput.setObjectName("edgesInput")
        self.edgesInput.setFont(font)
        self.edgesInput.setText("(0,1),(2,0),(1,2)")

    def _confirmHandler(self, points: str):
        obj_name = self.objectNameInput.text()
        if obj_name == "":
            return
        
        coordinates = self._str_to_list(points)
        edges = self._str_to_list(self.edgesInput.text())
        print("coordinates", coordinates)
        print("edges", edges)

        self.createObject(coordinates, self.objectNameInput.text())
        self.closeModal()

    def _str_to_list(self, string) -> list:
        string = string.split("),(")
        string = [p.replace(" ", "").replace("(", "").replace(")", "") for p in string]
        string = [p.split(",") for p in string]
        formated = []
        for t in string:
            f = []
            for point in t:
                f.append(float(point))
            formated.append(f)
            
        return formated