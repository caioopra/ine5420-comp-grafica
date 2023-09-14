from os import listdir

from PyQt5 import QtCore, QtGui, QtWidgets

from utils.readObjFile import readObjFile


class OpenFileModal:
    def setupUi(
        self,
        MainWindow,
        closeModal,
        setWindowDimensions,
        getObjectsFromFile,
        saveObjectsToFile,
    ):
        self.closeModal = closeModal
        self.setWindowDimensions = setWindowDimensions
        self.getObjectsFromFile = getObjectsFromFile
        self.saveObjectsToFile = saveObjectsToFile

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 350)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(11)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.filesList = QtWidgets.QListWidget(MainWindow)  # may need to create frame
        self.filesList.setGeometry(QtCore.QRect(10, 10, 380, 250))
        self.filesList.setFont(font)
        self.filesList.setObjectName("filesList")
        self.addFilesToList()
        self.filesList.doubleClicked.connect(
            lambda: self.openFile(self.filesList.currentItem().text())
        )

        self.filenameInput = QtWidgets.QLineEdit(MainWindow)
        self.filenameInput.setGeometry(QtCore.QRect(210, 280, 180, 25))
        self.filenameInput.setFont(font)

        self.saveButton = QtWidgets.QPushButton(MainWindow)
        self.saveButton.setGeometry(QtCore.QRect(10, 280, 180, 25))
        self.saveButton.setFont(font)
        self.saveButton.setText("Save current objects")
        self.saveButton.clicked.connect(
            lambda: self.saveObjectsToFile(self.filenameInput.text())
        )
        self.saveButton.adjustSize()

    def addFilesToList(self) -> None:
        files = listdir("objects")
        files = list(filter((lambda x: ".obj" in x), files))

        for file in files:
            self.filesList.addItem(file)
            
        self.closeModal()

    def openFile(self, filename: str) -> None:
        objects, window = readObjFile(filename)

        self.setWindowDimensions(window[0], window[1])
        self.getObjectsFromFile(objects)
        self.closeModal()
