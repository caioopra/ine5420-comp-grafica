from structures.Line import Line
from structures.Wireframe import Wireframe
from structures.Window import Window


class DisplayFile:
    def __init__(self):
        self.__points = []
        self.__lines = []
        self.__wireframes = []
        self.__buffer = None

        self.__window = Window()

    def getWindow(self) -> Window:
        return self.__window

    def getBuffer(self):
        return self.__buffer

    def getPoints(self) -> list:
        return self.__points

    def getLines(self) -> list:
        return self.__lines

    def getWireframes(self) -> list:
        return self.__wireframes

    def clearBuffer(self):
        self.__buffer = None

    def addToBuffer(self, objectType: str, buffer) -> None:
        if objectType == "LINE":
            if self.__buffer is not None:
                self.__buffer.addPoint(buffer)
            else:
                self.__buffer = Line(buffer, window=self.__window)
        elif objectType == "WIREFRAME":
            if self.__buffer is not None:
                self.__buffer.addPoint(buffer)
            else:
                self.__buffer = Wireframe(buffer, window=self.__window)
        else:
            self.__buffer = buffer

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

    def tryRegistering(self, currentType: str, objectName: str, color) -> str:
        if self.__buffer is None:
            return {"status": False, "mensagem": f"[ERROR] Draw an object first."}

        if objectName == "":
            return {
                "status": False,
                "mensagem": f"[ERROR] Enter a name before creating the object.",
            }

        if not self.verifyIfNameIsValid(objectName):
            return {
                "status": False,
                "mensagem": f"[ERROR] {objectName} is already being used.",
            }

        self.registerObject(currentType, objectName, color)
        return {"status": True, "mensagem": f"{objectName} ({currentType}) registered."}

    def registerObject(self, currentType: str, objectName: str, color) -> None:
        self.__buffer.setName(objectName)
        self.__buffer.setColor(color)
        print("buffer: ", self.__buffer)
        print("color for buffer: ", color)
        print("color in buffer", self.__buffer.getColor())
        if currentType == "POINT":
            self.__points.append(self.__buffer)
        elif currentType == "LINE":
            self.__lines.append(self.__buffer)
        elif currentType == "WIREFRAME":
            self.__wireframes.append(self.__buffer)

        self.__buffer = None
        
    def deleteObject(self, name: str) -> None:
        print(name)
        for i, point in enumerate(self.__points):
            if point.getName() == name:
                print("deleting")
                del self.__points[i]
                return

        for i, line in enumerate(self.__lines):
            if line.getName() == name:
                print("deleting")
                del self.__lines[i]
                return
                
        for i, wireframe in enumerate(self.__wireframes):
            if wireframe.getName() == name:
                print("deleting")
                del self.__wireframes[i]
                return

    def navigate(self, direction: str):
        self.__window.navigate(direction)

    def zoom(self, direction: str):
        self.__window.zoom(direction)

    def getBuffer(self):
        return self.__buffer

displayFile = DisplayFile()
