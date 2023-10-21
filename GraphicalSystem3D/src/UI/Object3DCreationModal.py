from PyQt5 import QtCore, QtGui, QtWidgets


class Object3DCreationModal(object):
    def setupUi(self, MainWindow, closeModal):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 300)
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
        self.pointsInput.setText("(0,0,0),(1, 1, 1)")

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

    def _confirmHandler(self, points: str):
        # points = points
        points = points.split("),(")
        points = [p.replace(" ", "").replace("(", "").replace(")", "") for p in points]
        points = [p.split(",") for p in points]
        formated = []
        for t in points:
            f = []
            for point in t:
                f.append(float(point))
            formated.append(tuple(f))

        print(formated)
