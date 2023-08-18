from Drawable import Drawable

class Point(Drawable):
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    def draw(self):
        pass

    def getX(self) -> float:
        return self.__x

    def getY(self) -> float:
        return self.__y

    def __str__(self) -> str:
        return f"({self.getX()}, {self.getY()})"

