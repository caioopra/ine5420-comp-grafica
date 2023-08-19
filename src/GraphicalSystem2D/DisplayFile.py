from structures.Point import Point
from structures.Line import Line
from structures.Wireframe import Wireframe


class DisplayFile:
    def __init__(self):
        self.__points = []
        self.__lines = []
        self.__wireframes = []

        self.__buffer = None

    def clearBuffer(self):
        self.__buffer = None

    def addToBuffer(self, objectType: str, buffer: Point) -> None:
        if objectType == "LINE":
            if self.__buffer is not None:
                self.__buffer.addPoint(buffer)
            else:
                self.__buffer = Line(buffer)
        elif objectType == "WIREFRAME":
            if self.__buffer is not None:
                self.__buffer.addPoint(buffer)
            else:
                self.__buffer = Wireframe(buffer)
        else:
            self.__buffer = buffer

    def getBuffer(self) -> Point | Line | Wireframe:
        return self.__buffer

    def verifyIfNameIsValid(self, name: str) -> bool:
        for point in self.__points:
            print(point.getName())
            if point.getName() == name:
                return False
        for line in self.__lines:
            if line.getName() == name:
                return False
        for wireframe in self.__wireframes:
            if wireframe.getName() == name:
                return False

        return True

    def tryRegistering(self, currentType: str, objectName: str) -> str:
        if self.__buffer is None:
            return f"[ERROR] Draw a object first."

        if objectName == "":
            return f"[ERROR] Enter a name before creating the object."

        if not self.verifyIfNameIsValid(objectName):
            return f"[ERROR] {objectName} is already being used."

        self.registerObject(currentType, objectName)
        return f"{objectName} ({currentType}) registered."

    def registerObject(self, currentType: str, objectName: str) -> None:
        self.__buffer.setName(objectName)
        if currentType == "POINT":
            self.__points.append(self.__buffer)
        elif currentType == "LINE":
            self.__lines.append(self.__buffer)
        elif currentType == "WIREFRAME":
            self.__buffer.removeLastLine()
            self.__wireframes.append(self.__buffer)

        self.__buffer = None

    def getPoints(self) -> list:
        return self.__points

    def getLines(self) -> list:
        return self.__lines

    def getWireframes(self) -> list:
        return self.__wireframes


displayFile = DisplayFile()
