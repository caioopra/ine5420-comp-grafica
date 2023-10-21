import sys
from UI.MainWindow import Ui_MainWindow
from PyQt5 import QtWidgets

from utils.writeObjFile import writeObjectsToFile
from structures.Point import Point
from structures.Line import Line
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    # objects = [Point(1, 2, name="asdasds"), Line(Point(3, 4), Point(9, 10), name="line"), Point(30, 2.2, name="brabo")]
    # objects[1].setColor("#00ff00")
    # teste = writeObjectsToFile("file", objects, [400, 300])
