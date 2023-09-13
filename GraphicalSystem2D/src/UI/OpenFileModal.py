from os import listdir

from PyQt5 import QtCore, QtGui, QtWidgets

from utils.readObjFile import readObjFile


class OpenFileModal:
    def setupUi(self, MainWindow, closeModal, setWindowDimensions, getObjectsFromFile):
        self.closeModal = closeModal
        self.setWindowDimensions = setWindowDimensions
        self.getObjectsFromFile = getObjectsFromFile

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
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

    def addFilesToList(self) -> None:
        files = listdir("objects")
        files = list(filter((lambda x: ".obj" in x), files))

        for file in files:
            self.filesList.addItem(file)

    def openFile(self, filename: str) -> None:
        objects, window = readObjFile(filename)

        self.setWindowDimensions(window[0], window[1])
        self.getObjectsFromFile(objects)
        self.closeModal()
