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
        self.pointsInput.setText("(0,0,0),(100,0,0),(0,100,0),(100,100,0)")

        self.confirmTransformButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmTransformButton.setGeometry(QtCore.QRect(10, 85, 130, 25))
        self.confirmTransformButton.setObjectName("confirmTransformButton")
        self.confirmTransformButton.setFont(font)
        self.confirmTransformButton.setText("Confirm")
        self.confirmTransformButton.clicked.connect(
            lambda: self._confirmHandler(self.pointsInput.text(), self.edgesInput.text())
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
        self.edgesInput.setText("(0,1),(1,3),(0,2),(2,3)")

    def _confirmHandler(self, points: str, edges:str):
        obj_name = self.objectNameInput.text()
        if obj_name == "":
            return
        print(points)
        points = points.split("),(")
        edges = edges.split("),(")
        print(edges)
        points = [p.replace(" ", "").replace("(", "").replace(")", "") for p in points]
        edges = [e.replace(" ", "").replace("(", "").replace(")", "") for e in edges]
        points = [p.split(",") for p in points]
        edges = [e.split(",") for e in edges]
        print(points)
        print(edges)
        formated_points = []
        formated_edges = []
        for t in points:
            f = []
            for point in t:
                f.append(int(point))
            formated_points.append(f)
        for t in edges:
            f = []
            for point in t:
                f.append(int(point))
            formated_edges.append(f)

        print("formated points:", formated_points)
        print("formated edges:", formated_edges)
        self.createObject(formated_points, formated_edges, self.objectNameInput.text())

        self.closeModal()

#d = ((xb-xa)**2 + (yb-ya)**2 + (zb-za)**2)**(1/2)
#
# ((0,0,0),(1, 1, 1),(2,2,2));(300,300,300),(301,301,301),(302,302,302))
#((200,200,200),(260,240,270),(320,230,300));(300,300,300),(320,340,370),(300,500,400))
