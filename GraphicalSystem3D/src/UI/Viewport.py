from PyQt5 import QtCore, QtGui, QtWidgets

from structures.Point import Point
from DisplayFile import displayFile

from utils.viewportTransformation import transformToWorldCoordinates
from utils.clipping.clipping import clip
from structures.BezierBicubicSurface import BezierBicubicSurface


class Viewport(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Viewport, self).__init__(parent)
        self.setMouseTracking(True)
        self.__currentColor = QtCore.Qt.red
        self.currentSelectedType = ""
        self.currentClippingMethod = ""

    def mousePressEvent(self, event):
        print("Current type: ", self.currentSelectedType)
        x, y = transformToWorldCoordinates(
            event.x(), event.y(), displayFile.getWindow()
        )
        if self.currentSelectedType != "":
            z = 0
            point = Point(x, y, z, displayFile.getWindow())
            normal_x, normal_y = displayFile.calculateNormalizedCoordinates(point)
            point.setNormalCoordinates(normal_x, normal_y)

        if self.currentSelectedType == "POINT":
            displayFile.addToBuffer(
                "POINT",
                point,
            )

        elif self.currentSelectedType == "LINE":
            displayFile.addToBuffer(
                "LINE",
                point,
            )
        elif self.currentSelectedType == "WIREFRAME":
            displayFile.addToBuffer(
                "WIREFRAME",
                point,
            )
        elif self.currentSelectedType == "BSPLINE":
            displayFile.addToBuffer(
                "BSPLINE",
                point,
            )
        elif self.currentSelectedType == "BEZIER_CURVE":
            displayFile.addToBuffer(
                "BEZIER_CURVE",
                point,
            )
        else:
            print("select a type first")

        self.update()

    def paintEvent(self, ev):
        qp = QtGui.QPainter(self)
        qp.setRenderHint(QtGui.QPainter.Antialiasing)

        brush = QtGui.QBrush(self.__currentColor)
        brush.setStyle(QtCore.Qt.SolidPattern)
        qp.setPen(self.__currentColor)
        qp.setBrush(brush)
        
        if displayFile.getBuffer() is not None:
            if isinstance(displayFile.getBuffer(), list):
                for point in displayFile.getBuffer():
                    normal_x, normal_y = displayFile.calculateNormalizedCoordinates(
                        point
                    )
                    point.setNormalCoordinates(normal_x, normal_y)
                
            elif not isinstance(displayFile.getBuffer(), Point):
                points = displayFile.getBuffer().getPoints()
                for point in points:
                    if point is not None:
                        normal_x, normal_y = displayFile.calculateNormalizedCoordinates(
                            point
                        )
                        point.setNormalCoordinates(normal_x, normal_y)
            else:
                normal_x, normal_y = displayFile.calculateNormalizedCoordinates(
                    displayFile.getBuffer()
                )
                displayFile.getBuffer().setNormalCoordinates(normal_x, normal_y)
                
        # for point in displayFile.getPoints():
        #     normal_x, normal_y = displayFile.calculateNormalizedCoordinates(point)
        #     point.setNormalCoordinates(normal_x, normal_y)

        # for line in displayFile.getLines():
        #     for point in line.getPoints():
        #         normal_x, normal_y = displayFile.calculateNormalizedCoordinates(point)
        #         point.setNormalCoordinates(normal_x, normal_y)

        # for wireframe in displayFile.getWireframes():
        #     for point in wireframe.getPoints():
        #         normal_x, normal_y = displayFile.calculateNormalizedCoordinates(point)
        #         point.setNormalCoordinates(normal_x, normal_y)

        to_draw_objects = clip(self.currentClippingMethod)
        print("all draw", to_draw_objects)
        to_draw_objects.append(BezierBicubicSurface((Point(124,113,0), Point(291,152,0), Point(479,151,0), Point(618,88,0), Point(127, 198, 0), Point(250,222,0), Point(439,215,0), Point(583,193,0), Point(132,255,0), Point(272,279,0), Point(467,280,0), Point(635,249,0), Point(131,378,0), Point(302,424,0), Point(490,408,0), Point(678,351,0))))
        for obj in to_draw_objects:
            if obj.getWindow() is None:
                obj.setWindow(displayFile.getWindow())
            print("Current draw", obj)
            if obj is displayFile.getBuffer():
                pen = QtGui.QPen(self.__currentColor, 3)
                qp.setPen(pen)
            else:
                pen = QtGui.QPen(obj.getColor(), 3)
                qp.setPen(pen)
                brush = QtGui.QBrush(obj.getColor())
                qp.setBrush(brush)
            obj.draw(qp)

    def getCurrentColor(self) -> None:
        return self.__currentColor

    def setCurrentColor(self, color) -> None:
        self.__currentColor = color

    def setCurrentClippingMethod(self, type: str) -> None:
        self.currentClippingMethod = type
        self.update()
