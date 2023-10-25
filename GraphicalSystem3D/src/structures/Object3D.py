from structures.Drawable import Drawable
from structures.Point import Point
from structures.Line import Line
from structures.Wireframe import Wireframe

class Object3D(Drawable):
    def __init__(self, name: str, coordinates: list[Point], window=None, faces:list=None, edges:list=None):
        super().__init__(name)
    
        self.window = window
        self.faces = faces
        self.edges = edges
        
        self.edges_lines = []
        for edge in self.edges:
            first = edge[0] - 1
            first_point = Point(coordinates[first][0], coordinates[first][1], window=window)
            second = edge[1] - 1
            second_point = Point(coordinates[second][0], coordinates[second][1], window=window)
            
            line = Line(first_point, second_point, window=window)
            self.edges_lines.append(line)
        
        self.faces_wireframes = []
        for face in self.faces:
            coords = []
            for edge in face:
                coords.extend(self.edges_lines[edge - 1].getCoordinates())
            
            wireframe = Wireframe(coords[0], window=window)
            wireframe.setpoints(coords[1:])
            self.faces_wireframes.append(wireframe)

    def draw(self):
        pass
    
    def applyTransformations(self, matrix) -> None:
        pass

    def calculateGeometricCenter(self) -> list:
        pass