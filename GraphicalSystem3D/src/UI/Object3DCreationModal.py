from PyQt5 import QtCore, QtGui, QtWidgets


class Object3DCreationModal(object):
    def setupUi(self, MainWindow, closeModal, createObject):
        self.closeModal = closeModal
        self.createObject = createObject
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

    def _confirmHandler(self, points: str):
        obj_name = self.objectNameInput.text()
        if obj_name == "":
            return

        points = points.split("),(")
        points = [p.replace(" ", "").replace("(", "").replace(")", "") for p in points]
        points = [p.split(",") for p in points]
        formated = []
        for t in points:
            f = []
            for point in t:
                f.append(int(point))
            formated.append(f)

        print(formated)
        self.createObject(f, self.objectNameInput.text())
        self.closeModal()

#from PyQt5 import QtCore, QtGui, QtWidgets


class Object3DCreationModal(object):
    def setupUi(self, MainWindow, closeModal, createObject):
        self.closeModal = closeModal
        self.createObject = createObject
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

    def _confirmHandler(self, clouds: str):
        obj_name = self.objectNameInput.text()
        if obj_name == "":
            return
        clouds = clouds.split(");(")
        formated_clouds = []
        for cloud in clouds:
            print(cloud)
            points = cloud.split("),(")
            points = [p.replace(" ", "").replace("(", "").replace(")", "") for p in points]
            points = [p.split(",") for p in points]
            formated = []
            for t in points:
                f = []
                for point in t:
                    f.append(int(point))
                formated.append(f)

            print("formated:", formated)
            print("f:", f)
            formated_clouds.append(formated)
            self.createObject(formated, self.objectNameInput.text())
            
        for i in range(len(formated_clouds)-1):
            for point in formated_clouds[i]:
                shortest_dist = float('inf')
                points = []
                for point2 in formated_clouds[i+1]:
                    point1_point2_distance = ((point[0]-point2[0])**2 + (point[1]-point2[1])**2 + (point[2]-point2[2])**2)**(1/2)
                    if shortest_dist > point1_point2_distance:
                        shortest_dist = point1_point2_distance
                        points = [point, point2]
                self.createObject(points, self.objectNameInput.text())
                print(points)
                print("criada uma linha entre", points[0], "e", points[1])
 
        self.closeModal()

#d = ((xb-xa)**2 + (yb-ya)**2 + (zb-za)**2)**(1/2)
#
# ((0,0,0),(1, 1, 1),(2,2,2));(300,300,300),(301,301,301),(302,302,302))
#((200,200,200),(260,240,270),(320,230,300));(300,300,300),(320,340,370),(300,500,400))