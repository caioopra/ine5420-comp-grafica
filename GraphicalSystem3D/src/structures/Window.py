from copy import copy
import numpy as np

import consts

from structures.Point import Point
from utils.matrixOperations import parallel_projection


class Window:
    def __init__(self):
        # self.createCoordinates()
        self.xw_min = consts.VIEWPORT_X_MIN
        self.yw_min = consts.VIEWPORT_Y_MIN
        self.xw_max = consts.VIEWPORT_X_MAX
        self.yw_max = consts.VIEWPORT_Y_MAX
        self.zw_min = 0
        self.zw_max = 0

        self.step = 10  # amount of pixels
        self.rotation_zoom_percentage = 10

    def setRotationZoomPercentage(self, value) -> None:
        if value == "":
            self.rotation_zoom_percentage = 0
            return

        self.rotation_zoom_percentage = int(value)

    def zoom(self, direction: str):
        if direction == "OUT":
            zoomAmount = 1 + self.rotation_zoom_percentage / 100
        else:
            zoomAmount = 1 - self.rotation_zoom_percentage / 100

        self.xw_min *= zoomAmount
        self.yw_min *= zoomAmount
        self.zw_min *= zoomAmount
        self.xw_max *= zoomAmount
        self.yw_max *= zoomAmount
        self.zw_max *= zoomAmount

    def navigate(self, direction):
        if direction == "UP":
            self.yw_min += self.step
            self.yw_max += self.step
        elif direction == "DOWN":
            self.yw_min -= self.step
            self.yw_max -= self.step
        elif direction == "RIGHT":
            self.xw_min += self.step
            self.xw_max += self.step
        elif direction == "LEFT":
            self.xw_min -= self.step
            self.xw_max -= self.step
        elif direction == "IN":
            self.zw_min -= self.step
            self.zw_max -= self.step
        elif direction == "OUT":
            self.zw_min += self.step
            self.zw_max += self.step    

    def getCenter(self) -> (int, int):
        return ((self.xw_max + self.xw_min)/2, (self.yw_max + self.yw_min)/2)

    def move_to_center(self):
        self.x_center = (self.xw_max + self.xw_min)/2
        self.y_center = (self.yw_max + self.yw_min)/2
        self.z_center = (self.zw_max + self.zw_min)/2
        self.xw_max -= self.x_center
        self.xw_min -= self.x_center
        self.yw_max -= self.y_center
        self.yw_min -= self.y_center
        self.zw_max -= self.z_center
        self.zw_min -= self.z_center

    def getMinsAndMaxes(self):
        return [self.yw_min, self.yw_max, self.xw_min, self.xw_max]
    
    def createCoordinates(self):
        p0 = Point(x=consts.VIEWPORT_X_MIN, y=consts.VIEWPORT_Y_MIN)  # L.D.
        p1 = Point(x=consts.VIEWPORT_X_MAX, y=consts.VIEWPORT_Y_MIN)  # R.D.
        p2 = Point(x=consts.VIEWPORT_X_MIN, y=consts.VIEWPORT_Y_MAX)  # L.U.
        p3 = Point(x=consts.VIEWPORT_X_MAX, y=consts.VIEWPORT_Y_MAX)  # R.U.
        self.window_coordinates = [p0, p1, p2, p3]
        
        self.window_coordinates_parallel_proj = copy(self.window_coordinates)
        
        transform = parallel_projection(self.window_coordinates)
        
        coords = []
        for p in self.window_coordinates:
            print(p.getAllCoordinates(), transform)
            m = np.dot(p.getAllCoordinates(), transform)
            coords.append(Point(x=m[0][0], y=m[0][1], z=m[0][2], window=self))
            
        self.window_coordinates[0] = coords[0]
        self.window_coordinates[1] = coords[1]
        self.window_coordinates[2] = coords[2]
        self.window_coordinates[3] = coords[3]    
        
            