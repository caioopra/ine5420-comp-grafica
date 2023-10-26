from structures.Point import Point
from structures.Line import Line
from structures.Wireframe import Wireframe
from structures.BezierCurve import BezierCurve
from structures.BSpline import BSpline
from structures.Window import Window

from PyQt5 import QtCore


class DisplayFile:
    def __init__(self):
        self.__points = []
        self.__lines = []
        self.__wireframes = []
        self.__curves = []
        self.__buffer = None

        self.__window = Window()

        self.addAxesLines()

    def getWindow(self) -> Window:
        return self.__window

    def setWindowSize(self, min: list, max: list) -> None:
        self.__window.xw_min = min[0]
        self.__window.yw_min = min[1]
        self.__window.xw_max = max[0]
        self.__window.yw_max = max[1]

    def getBuffer(self):
        return self.__buffer

    def getPoints(self) -> list:
        return self.__points

    def getLines(self) -> list:
        return self.__lines

    def getWireframes(self) -> list:
        return self.__wireframes

    def getCurves(self) -> list:
        return self.__curves

    def clearBuffer(self):
        self.__buffer = None

    def addAxesLines(self):
        points = [
            Point(-760, 0, self.__window),
            Point(760, 0, self.__window),
            Point(0, -490, self.__window),
            Point(0, 490, self.__window),
        ]
        for point in points:
            normal_x, normal_y = self.calculateNormalizedCoordinates(point)
            point.setNormalCoordinates(normal_x, normal_y)

        x_line = Line(
            pointA=points[0],
            pointB=points[1],
            name="x_axis",
            window=self.__window,
        )
        x_line.setColor(QtCore.Qt.black)
        y_line = Line(
            pointA=points[2],
            pointB=points[3],
            name="y_axis",
            window=self.__window,
        )
        y_line.setColor(QtCore.Qt.black)

        self.__lines.append(x_line)
        self.__lines.append(y_line)

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
        elif objectType == "BEZIER_CURVE":
            if self.__buffer is not None:
                self.__buffer.append(buffer)
            else:
                self.__buffer = [buffer]
        elif objectType == "BSPLINE":
            if self.__buffer is not None:
                self.__buffer.append(buffer)
            else:
                self.__buffer = [buffer]
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
        for curve in self.__curves:
            if curve.getName() == name:
                return False

        return True

    def getObjectByName(self, name: str) -> Point | Line | Wireframe:
        for point in self.__points:
            if point.getName() == name:
                return point

        for line in self.__lines:
            if line.getName() == name:
                return line

        for wireframe in self.__wireframes:
            if wireframe.getName() == name:
                return wireframe

        for curve in self.__curves:
            if curve.getName() == name:
                return curve

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
        if currentType == "BEZIER_CURVE":
            self.__curves.append(
                BezierCurve(
                    name=objectName,
                    coordinates=self.__buffer,
                    color=color,
                    window=self.__window,
                )
            )
        elif currentType == "BSPLINE":
            self.__curves.append(
                BSpline(
                    name=objectName,
                    coordinates=self.__buffer,
                    color=color,
                    window=self.__window,
                )
            )
        else:
            self.__buffer.setName(objectName)
            self.__buffer.setColor(color)

        if currentType == "POINT":
            self.__points.append(self.__buffer)
        elif currentType == "LINE":
            self.__lines.append(self.__buffer)
        elif currentType == "WIREFRAME":
            self.__wireframes.append(self.__buffer)

        self.__buffer = None
        
    def create3DObject(self, points: list[tuple], obj_name: str):
            print("Points:", points)
            self.__points = []
            # TODO: implement
            for point in points:
                print(point[0], point[1], point[2])
                ponto_criado = Point(point[0], point[1], point[2], obj_name)
                self.__points.append(ponto_criado)
            #print("z:", ponto_criado.getZ())
            if len(points) >= 3:
                wireframe = Wireframe(self.__points[0], window=self.__window)
                wireframe.setPoints(self.__points)
                self.__wireframes.append(wireframe)
                print("Creating 3D object...\n", points, obj_name)
            elif len(points) == 2:
                line = Line(self.__points[0], window=self.__window)
                line.setCoordinates(self.__points[0], self.__points[1])
                self.__lines.append(line)

    def addObjectFromFile(self, obj: Point | Line | Wireframe):
        if isinstance(obj, Point):
            self.__points.append(obj)
        elif isinstance(obj, Line):
            self.__lines.append(obj)
        elif isinstance(obj, Wireframe):
            self.__wireframes.append(obj)

    def deleteObject(self, name: str) -> None:
        for i, point in enumerate(self.__points):
            if point.getName() == name:
                del self.__points[i]
                return

        for i, line in enumerate(self.__lines):
            if line.getName() == name:
                del self.__lines[i]
                return

        for i, wireframe in enumerate(self.__wireframes):
            if wireframe.getName() == name:
                del self.__wireframes[i]
                return
        
        for i, curve in enumerate(self.__curves):
            if curve.getName() == name:
                del self.__curves[i]
                return

    def navigate(self, direction: str):
        self.__window.navigate(direction)

    def getCenter(self) -> (int, int):
        return self.__window.getCenter()

    def move_to_center(self):
        self.__window.move_to_center()

    def zoom(self, direction: str):
        self.__window.zoom(direction)

    def getBuffer(self):
        return self.__buffer

    def calculateNormalizedCoordinates(self, object):
        x = object.getX()
        y = object.getY()
        print("x:", x)
        print(y)
        yw_min, yw_max, xw_min, xw_max = self.__window.getMinsAndMaxes()
        normal_x = (x - xw_min) / (xw_max - xw_min) * 2 - 1
        normal_y = (y - yw_min) / (yw_max - yw_min) * 2 - 1
        return (normal_x, normal_y)


displayFile = DisplayFile()
