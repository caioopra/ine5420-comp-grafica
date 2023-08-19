from structures.Point import Point
from structures.Line import Line
from structures.Wireframe import Wireframe


class DisplayFile:
    def __init__(self):
        self.__points = []
        self.__lines = []
        self.__wireframes = []

        self.__buffer = None

    def setBuffer(self, buffer: Point | Line | Wireframe) -> None:
        self.__buffer = buffer

    def getBuffer(self) -> Point | Line | Wireframe:
        return self.__buffer

    def verifyIfNameIsValid(self, name: str) -> bool:
        for point in self.__points:
            if point.getName() == name:
                return False

        for line in self.__lines:
            if line.getName() == name:
                return False

        for wireframe in self.__wireframes:
            if wireframe.getName() == name:
                return False

        return True

    def registerObject(self, currentType: str) -> None:
        if currentType == "POINT":
            self.__points.append(self.__buffer)
        elif currentType == "LINE":
            self.__lines.append(self.__buffer)
        elif currentType == "POLYGON":
            self.__wireframes.append(self.__buffer)

        self.__buffer = None

    def getPoints(self) -> list:
        return self.__points

    def getLines(self) -> list:
        return self.__lines

    def getWireframes(self) -> list:
        return self.__wireframes


displayFile = DisplayFile()
